import pygame
from Configurations import Configurations

class Winner:
    """
    Clase que representa la animación de victoria del juego.
    Muestra una imagen estática durante unos segundos.
    """

    def __init__(self, screen: pygame.surface.Surface):
        """
        Inicializa la animación de victoria.
        :param screen: Superficie del juego.
        """
        self.screen = screen

        # Cargar imagen de victoria
        victory_image_path = "../media/winner.png"  # Asegúrate de colocar la imagen aquí
        self.image = pygame.image.load(victory_image_path)
        self.image = pygame.transform.scale(self.image, Configurations.get_screen_size())

        # Posicionar al centro
        self.rect = self.image.get_rect(center=screen.get_rect().center)

    def play(self):
        """
        Muestra la imagen de victoria durante unos segundos.
        """
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()
        pygame.time.delay(3000)  # Espera 3 segundos
