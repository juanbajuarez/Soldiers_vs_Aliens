import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from Soldier import Soldier

class Shot(Sprite):
    """
    Clase que representa un disparo generado por un soldado.
    Hereda de Sprite para integrarse al sistema de colisiones y grupos de pygame.
    """

    # ─────────────────────────────────────────────
    # 1. Constructor: carga frames y define posición del disparo
    # ─────────────────────────────────────────────
    def __init__(self, soldier: Soldier):
        """
        Inicializa un nuevo disparo a partir de la posición de un soldado.
        :param soldier: Objeto Soldier desde el que se dispara.
        """
        super().__init__()
        self.owner = soldier

        # Lista de frames de animación del disparo
        self._frames = []

        # ─── Cargar hoja de sprites de disparo ───
        sheet_path = Configurations.get_shot_sheet_path()
        shot_sheet = pygame.image.load(sheet_path)

        # ─── Datos de recorte ───
        frames_per_row = Configurations.get_frames_per_row()
        sheet_width = shot_sheet.get_width()
        sheet_height = shot_sheet.get_height()
        frame_width = sheet_width // frames_per_row
        frame_height = sheet_height

        # ─── Escalar cada frame al tamaño configurado ───
        frame_size = Configurations.get_shot_size()

        for i in range(frames_per_row):
            x = i * frame_width
            rect = (x, 0, frame_width, frame_height)
            frame = shot_sheet.subsurface(rect)
            frame = pygame.transform.scale(frame, frame_size)
            self._frames.append(frame)

        # ─── Inicialización de animación ───
        self._last_update_time = pygame.time.get_ticks()
        self._frame_index = 0
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # ─── Posición inicial del disparo (desde el soldado) ───
        self.rect = self.image.get_rect()
        self.rect.right = soldier.rect.left
        self.rect.centery = soldier.rect.centery

        self._rect_x = float(self.rect.x)
        self._rect_y = float(self.rect.y)

        # ─── Velocidad del disparo ───
        self._speed = Configurations.get_soldier_speed()

    # ─────────────────────────────────────────────
    # 2. Movimiento del disparo
    # ─────────────────────────────────────────────
    def update_position(self, screen: pygame.surface.Surface) -> None:
        """
        Actualiza la posición horizontal del disparo.
        :param screen: Superficie para verificar límites si es necesario.
        """
        self._rect_x -= self._speed
        self.rect.x = int(self._rect_x)

    # ─────────────────────────────────────────────
    # 3. Animación del disparo
    # ─────────────────────────────────────────────
    def update_animation(self) -> None:
        """
        Cambia el frame visible del disparo con base en el tiempo.
        """
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frame_delay()

        if (current_time - self._last_update_time) >= frame_delay:
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            # Reinicia animación si llega al final
            if self._frame_index >= len(self._frames):
                self._frame_index = 0

    # ─────────────────────────────────────────────
    # 4. Dibujar disparo en pantalla
    # ─────────────────────────────────────────────
    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Dibuja el disparo en pantalla.
        :param screen: Superficie donde se dibuja.
        """
        screen.blit(self.image, self.rect)
