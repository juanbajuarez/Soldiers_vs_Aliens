import pygame
from Configurations import Configurations

class GameOverAnimation:
    """
    Clase que representa la animación del fin del juego.
    Carga una secuencia de frames desde una hoja de sprites, y una imagen final "GAME OVER".
    """

    # ───────────────────────────────────────────────────────
    # 1. Constructor: carga sprites de animación y la imagen final
    # ───────────────────────────────────────────────────────
    def __init__(self, screen: pygame.surface.Surface):
        """
        Inicializa los frames de animación de Game Over.
        :param screen: Superficie donde se mostrará la animación.
        """
        self._frames = []

        # ─── Cargar hoja de sprites de muerte ───
        sheet_path = Configurations.get_soldier_kill()
        game_over_sheet = pygame.image.load(sheet_path)

        # ─── Obtener dimensiones del frame ───
        frames_per_row = Configurations.get_frames_per_row_kills()
        sheet_width = game_over_sheet.get_width()
        sheet_height = game_over_sheet.get_height()
        frame_width = sheet_width // frames_per_row
        frame_height = sheet_height
        frame_size = Configurations.get_game_over_size()

        # ─── Recortar y escalar los frames de animación ───
        for i in range(frames_per_row):
            x = i * frame_width
            y = 0
            rect = (x, y, frame_width, frame_height)
            frame = game_over_sheet.subsurface(rect)
            frame = pygame.transform.scale(frame, frame_size)
            self._frames.append(frame)

        # ─── Cargar imagen final "GAME OVER" ───
        final_path = Configurations.get_game_over_image_path()
        final_image = pygame.image.load(final_path)
        final_image = pygame.transform.scale(final_image, frame_size)
        self._frames.append(final_image)

        # ─── Inicialización de estado de animación ───
        self._last_update_time = pygame.time.get_ticks()
        self._frame_index = 0
        self.image = self._frames[self._frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center

    # ───────────────────────────────────────────────────────
    # 2. Métod0 de reproducción de la animación
    # ───────────────────────────────────────────────────────
    def play(self) -> None:
        """
        Reproduce todos los frames de la animación centrada.
        Muestra la imagen "GAME OVER" al final con mayor duración.
        """
        screen = pygame.display.get_surface()
        screen_rect = screen.get_rect()

        for i, frame in enumerate(self._frames):
            # Limpiar pantalla
            screen.fill((0, 0, 0))

            # Centrar y dibujar frame
            self.image = frame
            self.rect = self.image.get_rect(center=screen_rect.center)
            screen.blit(self.image, self.rect)

            # Mostrar frame en pantalla
            pygame.display.flip()

            # Pausa entre frames (último frame más tiempo)
            pygame.time.delay(300 if i < len(self._frames) - 1 else 2000)
