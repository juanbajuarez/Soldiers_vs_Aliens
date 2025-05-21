# bits & bytes
# Fecha: Mayo de 2025
# Descripción: version 02 Juego del gato.
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
    #Fondo de la pantalla en rgb
    screen.fill(Configurations.get_background())

    # Se actualiza la pantalla
    pygame.display.flip()