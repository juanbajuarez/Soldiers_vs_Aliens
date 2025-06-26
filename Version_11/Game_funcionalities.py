import pygame
from Configurations import Configurations
from Media import Background
from Soldier import Soldier
from Shot import Shot
from Alien import Alien
from random import randint


def game_events(soldier: Soldier,
                shots: pygame.sprite.Group,
                audio) -> bool:  # Nuevo parámetro
    """
    Maneja los eventos del juego con sonidos.
    """
    game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True

            if event.key == pygame.K_SPACE and len(shots) < 2:
                shots.add(Shot(soldier))
                audio.play_sound('shot')  # Sonido de disparo
                soldier.shoots()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False

    return game_over


def check_collisions(screen: pygame.surface.Surface,
                     soldier: Soldier,
                     shots: pygame.sprite.Group,
                     aliens: pygame.sprite.Group,
                     score,
                     audio) -> bool:  # Nuevo parámetro
    """
    Verifica colisiones con efectos de sonido.
    """
    game_over = False
    screen_rect = screen.get_rect()

    # Colisiones disparo-alien
    collisions = pygame.sprite.groupcollide(shots, aliens, True, True)

    if collisions:
        audio.play_sound('alien_hit')  # Sonido de impacto
        for aliens_hit in collisions.values():
            score.increase()

    # Limpieza de aliens y disparos
    for alien in aliens.copy():
        if alien.rect.left > screen_rect.right:
            aliens.remove(alien)

    for shot in shots.copy():
        if shot.rect.right < screen_rect.left:
            shots.remove(shot)

    # Colisión soldado-alien
    if pygame.sprite.spritecollide(soldier, aliens, False):
        audio.play_sound('game_over')  # Sonido de derrota
        game_over = True

    # Generación de nuevos aliens
    if len(aliens) <= Configurations.get_min_aliens():
        for _ in range(randint(0, 5)):
            aliens.add(Alien(screen))

    return game_over


def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock,
                   background: Background,
                   soldier: Soldier,
                   shots: pygame.sprite.Group,
                   aliens: pygame.sprite.Group,
                   score) -> None:
    """
    Actualiza la pantalla (sin cambios en la lógica de audio).
    """
    background.blit(screen)

    for shot in shots:
        shot.update_position(screen)
        shot.update_animation()
        shot.blit(screen)

    for alien in aliens:
        alien.update_position(screen)
        alien.update_animation()
        alien.blit(screen)

    soldier.update_position(screen)
    soldier.update_animation()
    soldier.blit(screen)

    score.draw(screen)

    pygame.display.flip()
    clock.tick(Configurations.get_fps())



