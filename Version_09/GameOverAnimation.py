import pygame
import os
from Configurations import Configurations

class GameOverAnimation:
    """
    Clase que representa la animación del fin del juego.
    Carga una secuencia de imágenes y las reproduce con un pequeño retardo.
    """

    def __init__(self, screen: pygame.surface.Surface):
        """
        Constructor de la clase.
        :param screen: Superficie de la pantalla donde se mostrará la animación.
        """
        self.screen = screen
        self.frames = []
        self.load_frames()
        self.frame_delay = 200  # milisegundos entre cada frame

    def load_frames(self):
        """
        Carga los frames desde la ruta especificada en Configurations.
        """
        folder = Configurations.get_game_over_frames_folder()
        total_frames = Configurations.get_game_over_frame_count()
        screen_size = Configurations.get_screen_size()

        for i in range(1, total_frames + 1):
            frame_path = os.path.join(folder, f"frame{i}.png")
            image = pygame.image.load(frame_path)
            image = pygame.transform.scale(image, screen_size)
            self.frames.append(image)

    def play(self):
        """
        Reproduce la animación de fin de juego una sola vez.
        """
        clock = pygame.time.Clock()

        for frame in self.frames:
            self.screen.blit(frame, (0, 0))
            pygame.display.flip()
            pygame.time.delay(self.frame_delay)
            clock.tick(Configurations.get_fps())
