# Juan Bautista Juárez
# Fecha: 21 de Mayo de 2025
# Descripción: version 05 Juego del alien
from time import sleep

import pygame
from Configurations import Configurations
from Game_functionalities import game_event,screen_refresh,check_collitions
from Media import Background
from Soldier import Soldier
from pygame.sprite import Group
from Alien import Alien
from random import randint
def run_game()->None:
    """
    Función principal.
    :return: Nada.
    """
    #Inicia modulo pygame
    pygame.init()
    screen_size=Configurations.get_screen_size()
    # Se inicializa la pantalla
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())
    clock = pygame.time.Clock()

    background = Background()
    soldier = Soldier(screen)
    """Nuevo"""
    aliens=Group()
    min_aliens=Configurations.get_min_aliens()
    aliens_to_spawn=min_aliens+randint(0,8)
    for _ in range(aliens_to_spawn):
        alien=Alien(screen)
        aliens.add(alien)

    #Se crea el grupo para los shots
    #Mofificar estas líneas para que se aplique a los grupos
    gunshots=Group()
    # Ciclo principal del juego


    game_over = False

    while not game_over:
        game_over = game_event(soldier,gunshots,screen)
        if game_over:
            break
        # Se dibuja los elementos gráficos en la pantalla
        screen_refresh(screen, clock, background,soldier,gunshots,aliens)
        if game_over:
            sleep(3)
        game_over=check_collitions(screen,soldier,gunshots,aliens)
    pygame.quit()


# Código a nivel módulo.
if __name__ == '__main__':
    run_game()