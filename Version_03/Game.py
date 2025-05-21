# bits & bytes
# Fecha: Mayo de 2025
# Descripción: version 03 Juego del gato

import pygame
from Configurations import Configurations
from Game_functionalities import game_event,screen_refresh
from Media import Background

def run_game()->None:
    """
    Función principal.
    :return:Nada.
    """
    #Inicia modulo pygame
    pygame.init()

    #Se inicializa la pantalla
    screen=pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())
    clock = pygame.time.Clock()

    background=Background()
    #Ciclo principal del juego

    game_over=False

    while not game_over:
        game_over = game_event()
        # Se dibuja los elementos gráficos en la pantalla
        screen_refresh(screen,clock,background)
        # Se cierran los recursos del juego
    pygame.quit()

#Código a nivel módulo.
if __name__ == '__main__':
    run_game()