"""
Nombre: Durán Breceda Lourdes Jamileth y Bautista Juárez Juan
Fecha: 23 junio 2025
Versión 13:
"""


from time import sleep
import pygame
from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh, check_collisions,handle_powerups
from Media import Background
from Soldier import Soldier
from Soldier2 import Soldier2
from Alien import Alien
from GameOverAnimation import GameOverAnimation
from Score import Score
from AudioManager import AudioManager
from random import randint
from pygame.sprite import Group
from PowerUp import PowerUp
from Winner import Winner


def run_game() -> None:
    """
    Función principal del juego. Inicializa, ejecuta el bucle principal y gestiona el final del juego.
    """
    pygame.init()
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())

    clock = pygame.time.Clock()
    background = Background()
    soldier = Soldier(screen)
    soldier2 = Soldier2(screen)
    shots = Group()
    aliens = Group()
    score = Score()
    audio = AudioManager()
    audio.play_music()
    powerups=Group()
    powerup_spawn_interval = Configurations.get_time_in_time_power()  # 5 segundos
    last_powerup_time = pygame.time.get_ticks()


    for _ in range(Configurations.get_min_aliens() + randint(0, 5)):
        aliens.add(Alien(screen))

    game_over = False
    while not game_over:
        # Manejo de eventos
        game_over = game_events(soldier, soldier2, shots, audio)

        if not game_over:
            # Colisiones y actualizaciones
            last_powerup_time = handle_powerups(screen, powerups, last_powerup_time, powerup_spawn_interval)
            game_over = check_collisions(screen, soldier, soldier2, shots, aliens, score, audio,powerups)
            screen_refresh(screen, clock, background, soldier, soldier2, shots, aliens, score,powerups)

        # Mostrar animación de Game Over
        if game_over:
            if score.score >= Configurations.get_winner():
                Winner(screen).play()
            else:
                GameOverAnimation(screen).play()
            sleep(1)


    audio.stop_music()
    pygame.quit()

# Código a nivel de módulo
if __name__ == "__main__":
    run_game() 