# Juan Bautista Juárez
# Fecha: 21 de Mayo de 2025
# Descripción: version 05 Juego del gato
# Funcionalidades del juego.

import pygame
from Configurations import Configurations
from Media import Background
from Soldier import Soldier
from Shot import Shot


def game_event(soldier:Soldier,shots:pygame.sprite.Group,screen)->bool:
    """
    Función que administra los eventos del juego.
    :return: La bandera del fin del juego
    """
    game_over=False
    # Se verifican los eventos(teclado y ratón) del juego
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                soldier.is_moving_up=True
            if event.key==pygame.K_DOWN:
                soldier.is_moving_down=True
            if event.key == pygame.K_SPACE:
                shot=Shot(screen,soldier)
                shot._is_moving_shot=True
                shots.add(shot)
                soldier.shoots()

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                soldier.is_moving_up=False
            if event.key==pygame.K_DOWN:
                soldier.is_moving_down=False
    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock: pygame.time.Clock,background:Background,soldier:Soldier,shots:pygame.sprite.Group)->None:
    """
    Función que administra los elementos visuales del juego

    """

    # Se dibuja el fondo de la pantalla
    background.blit(screen)
    soldier.update_animation()
    soldier.update_position(screen)
    soldier.blit(screen)

    if len(shots.sprites()) > 0:
        for shot in shots.sprites():
            shot.position_shot(screen)
            shot.animation_shot()
    shots.draw(screen)
    # Se actualiza la pantalla
    pygame.display.flip()
    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())