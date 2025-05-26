# Juan Bautista Juárez
# Fecha: 21 de Mayo de 2025
# Descripción: version 04 Juego del gato
# Funcionalidades del juego.

import pygame
from Configurations import Configurations
from Media import Background
from Soldier import Soldier


def game_event(soldier:Soldier)->bool:
    """
    Función que administra los eventos del juego.
    :return: La bandera del fin del juego
    """
    game_over=False
    # Se verifican los eventos(teclado y ratón) del juego
    for event in pygame.event.get():

        if event.type==pygame.KEYDOWN:
            if event.type==pygame.K_UP:
                soldier.is_moving_up=True
            if event.type==pygame.K_UP:
                soldier.is_moving_down=True
        if event.type==pygame.KEYUP:
            if event.type==pygame.K_UP:
                soldier.is_moving_up=False
            if event.type==pygame.K_UP:
                soldier.is_moving_down=False

         # Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True
    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock: pygame.time.Clock,background:Background,soldier:Soldier)->None:
    """
    Función que administra los elementos visuales del juego
    """

    # Se dibuja el fondo de la pantalla
    background.blit(screen)

    #actualiza la posicion
    soldier.update_position()

    #Se dibuja el soldado
    soldier.blit(screen)

    # Se actualiza la pantalla
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())