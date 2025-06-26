"""
Nombre: Durán Breceda Lourdes Jamileth y Bautista Juárez Juan
Fecha: 23 junio 2025
Versión 10:
-Se agregó pantalla de game over


"""
from time import sleep
import pygame
from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh, check_collisions
from Media import Background
from Soldier import Soldier
from Shot import Shot
from Alien import Alien
from GameOverAnimation import GameOverAnimation
from Score import Score
from AudioManager import AudioManager  # Nuevo import
from random import randint


def run_game() -> None:
    """Función principal del juego con sistema de audio integrado."""
    pygame.init()
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())

    # Inicializar sistemas
    clock = pygame.time.Clock()
    background = Background()
    soldier = Soldier(screen)
    shots = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    score = Score()
    audio = AudioManager()  # Nuevo gestor de audio

    # Iniciar música
    audio.play_music()

    # Generar aliens iniciales
    for _ in range(Configurations.get_min_aliens() + randint(0, 5)):
        aliens.add(Alien(screen))

    # Bucle principal
    game_over = False
    while not game_over:
        game_over = game_events(soldier, shots, audio)  # Pasar audio

        if not game_over:
            game_over = check_collisions(screen, soldier, shots, aliens, score, audio)  # Pasar audio
            screen_refresh(screen, clock, background, soldier, shots, aliens, score)

        if game_over:
            GameOverAnimation(screen).play()
            sleep(1)

    # Detener música al salir
    audio.stop_music()
    pygame.quit()


if __name__ == "__main__":
    run_game()