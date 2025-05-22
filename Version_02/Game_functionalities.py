# Juan Bautista Juárez
# Fecha: 21 de Mayo de 2025
# Descripción: version O2 Juego Soldados vs Aliens
# Funcionalidades del juego

import pygame
from Configurations import Configurations

def game_event()->bool:
    """
    Función que administra los eventos del juego.
    Return: La bandera del fin del juego.
    """
    game_over=False
    # Se verifican los eventos(teclado y ratón) del juego
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True
    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface)->None:
    """
    Función que administra los elementos visuales del juego
    """

    # Se dibuja el fondo de la pantalla
    screen.fill(Configurations.get_background())
    # Se actualiza la pantalla
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.