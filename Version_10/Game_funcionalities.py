import pygame
from Configurations import Configurations
from Media import Background
from Soldier import Soldier
from Shot import Shot
from Alien import Alien
from random import randint
from Score import Score



def game_events(soldier: Soldier, shots: pygame.sprite.Group) -> bool:
    """
    Función que administra los eventos del juego.
    :param soldier: Objeto con el soldado (personaje principal).
    :param shots:

    :return: La bandera de fin del juego.

    """
    # Se declara la bandera de fin del juego que se retorna.
    game_over = False

    # Se verifican los eventos (teclado y ratón) del juego.
    for event in pygame.event.get():
        # El evento es un clic para cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True


        # Se verifica el evento de presionar una tecla.
        if event.type == pygame.KEYDOWN:
            # Se verifica las flechas para el movimiento.
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True

            # Si se presionó el espacio, entonces se crea un nuevo disparo y se agrega al grupo. Además, indica que
            # el soldado está disparando.
            if event.key == pygame.K_SPACE and len(shots)<2:
                new_shot = Shot(soldier)
                shots.add(new_shot)
                soldier.shoots()


        # Se verifica el evento de soltar una tecla.
        if event.type == pygame.KEYUP:
            # Se verifica las flechas para dejar de moverse.
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False



    # Se regresa la bandera.
    return game_over


def check_collisions(screen: pygame.surface.Surface,
                     soldier: Soldier,
                     shots: pygame.sprite.Group,
                     aliens: pygame.sprite.Group,
                     score) -> bool:
    """
    Verifica colisiones y actualiza el marcador.

    Args:
        score (Score): Instancia del marcador a actualizar
    """
    game_over = False
    screen_rect = screen.get_rect()

    # Colisiones disparo-alien
    collisions = pygame.sprite.groupcollide(shots, aliens, True, True)

    # Actualizar marcador
    if collisions:
        for aliens_hit in collisions.values():
            score.increase()  # Incrementar por cada alien eliminado

    # Resto de lógica de colisiones (sin cambios)
    for alien in aliens.copy():
        if alien.rect.left > screen_rect.right:
            aliens.remove(alien)

    for shot in shots.copy():
        if shot.rect.right < screen_rect.left:
            shots.remove(shot)

    if pygame.sprite.spritecollide(soldier, aliens, False):
        game_over = True

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
    Actualiza pantalla incluyendo el marcador.
    """
    # Dibujar elementos existentes
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

    # Dibujar marcador (nuevo)
    score.draw(screen)

    pygame.display.flip()
    clock.tick(Configurations.get_fps())




