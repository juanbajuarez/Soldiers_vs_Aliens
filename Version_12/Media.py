import pygame
from Configurations import Configurations

class Background:
    """
    Clase que administra el fondo del juego.
    Carga la imagen de fondo, la escala al tamaño de la pantalla,
    y la dibuja durante cada frame del juego.
    """

    # ─────────────────────────────────────────────
    # 1. Constructor: carga y prepara el fondo
    # ─────────────────────────────────────────────
    def __init__(self):
        """
        Inicializa el fondo de pantalla cargando la imagen y ajustando su tamaño.
        """
        # ─── Ruta de la imagen ───
        image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(image_path)

        # ─── Escalado al tamaño de pantalla ───
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        # ─── Obtener rectángulo de posición ───
        self.rect = self.image.get_rect()

    # ─────────────────────────────────────────────
    # 2. Métod0 para dibujar el fondo
    # ─────────────────────────────────────────────
    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Dibuja la imagen de fondo sobre la superficie de juego.
        :param screen: Objeto Surface donde se renderiza el fondo.
        """
        screen.blit(self.image, self.rect)
