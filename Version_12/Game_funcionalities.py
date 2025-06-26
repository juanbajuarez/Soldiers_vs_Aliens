import pygame
from pygame.sprite import Group
from Configurations import Configurations
from Media import Background
from Soldier import Soldier
from Soldier2 import Soldier2
from Shot import Shot
from Alien import Alien
from Score import Score
from AudioManager import AudioManager
from random import randint

def game_events(soldier: Soldier,
                soldier2: Soldier2,
                shots: Group,
                audio: AudioManager) -> bool:
    """
    Procesa eventos de teclado para ambos jugadores.
    Retorna True si se debe cerrar el juego.
    """
    game_over = False
    controls = Configurations.get_second_player_controls()

    for event in pygame.event.get():
        # ─── Cierre del juego ───
        if event.type == pygame.QUIT:
            game_over = True

        # ─── Teclas presionadas ───
        if event.type == pygame.KEYDOWN:
            # Jugador 1
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True
            if event.key == pygame.K_SPACE and len(shots) <2:
                shots.add(Shot(soldier))
                audio.play_sound('shot')
                soldier.shoots()

            # Jugador 2
            if event.key == controls["move_up"]:
                soldier2.is_moving_up = True
            if event.key == controls["move_down"]:
                soldier2.is_moving_down = True
            if event.key == controls["shoot"] and len(shots) < 4:
                shots.add(Shot(soldier2))
                audio.play_sound('shot')
                soldier2.shoots()

        # ─── Teclas soltadas ───
        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False

            # Jugador 2
            if event.key == controls["move_up"]:
                soldier2.is_moving_up = False
            if event.key == controls["move_down"]:
                soldier2.is_moving_down = False

    return game_over

def check_collisions(screen: pygame.Surface,
                     soldier: Soldier,
                     soldier2: Soldier2,
                     shots: Group,
                     aliens: Group,
                     score: Score,
                     audio: AudioManager) -> bool:
    """
    Detecta colisiones entre:
    - disparos y aliens
    - jugadores y aliens
    También genera nuevos enemigos y determina si el juego termina.
    """
    game_over = False
    screen_rect = screen.get_rect()

    # ─── Colisiones disparo vs alien ───
    collisions = pygame.sprite.groupcollide(shots, aliens, True, True)
    if collisions:
        audio.play_sound('alien_hit')
        for _ in collisions.values():
            score.increase()

    # ─── Eliminar aliens fuera de pantalla ───
    for alien in aliens.copy():
        if alien.rect.left > screen_rect.right:
            aliens.remove(alien)

    # ─── Eliminar disparos fuera de pantalla ───
    for shot in shots.copy():
        if shot.rect.right < screen_rect.left or shot.rect.left > screen_rect.right:
            shots.remove(shot)

    # ─── Colisiones jugador vs alien ───
    if soldier.is_live and pygame.sprite.spritecollide(soldier, aliens, False):
        soldier.is_live = False
        audio.play_sound('game_over')

    if soldier2.is_live and pygame.sprite.spritecollide(soldier2, aliens, False):
        soldier2.is_live = False
        audio.play_sound('game_over')

    # ─── Game Over si ambos jugadores están muertos ───
    if not soldier.is_live and not soldier2.is_live:
        game_over = True

    # ─── Reposición de aliens ───
    if len(aliens) <= Configurations.get_min_aliens():
        for _ in range(randint(0, 5)):
            aliens.add(Alien(screen))

    return game_over

def screen_refresh(screen: pygame.Surface,
                   clock: pygame.time.Clock,
                   background: Background,
                   soldier: Soldier,
                   soldier2: Soldier2,
                   shots: Group,
                   aliens: Group,
                   score: Score) -> None:
    """
    Redibuja todos los elementos del juego por frame:
    fondo, disparos, enemigos, jugadores y puntaje.
    """
    # ─── Dibujar fondo ───
    background.blit(screen)

    # ─── Disparos ───
    for shot in shots:
        shot.update_position(screen)
        shot.update_animation()
        shot.blit(screen)

    # ─── Aliens ───
    for alien in aliens:
        alien.update_position(screen)
        alien.update_animation()
        alien.blit(screen)

    # ─── Jugador 1 ───
    if soldier.is_live:
        soldier.update_position(screen)
        soldier.update_animation()
        soldier.blit(screen)

    # ─── Jugador 2 ───
    if soldier2.is_live:
        soldier2.update_position(screen)
        soldier2.update_animation()
        soldier2.blit(screen)

    # ─── Puntaje ───
    score.draw(screen)

    # ─── Actualizar pantalla ───
    pygame.display.flip()
    clock.tick(Configurations.get_fps())
