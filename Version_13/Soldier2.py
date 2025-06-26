import pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class Soldier2(Sprite):
    """
    Clase que representa un soldado (personaje principal).
    """

    # ─────────────────────────────────────────────
    # 1. Constructor
    # ─────────────────────────────────────────────
    def __init__(self, screen: pygame.surface.Surface):
        """
        Constructor del soldado.
        :param screen: Superficie del juego.
        """
        super().__init__()

        # Banderas de estado
        self._is_moving_up = False
        self._is_moving_down = False
        self._is_shooting = False
        self._is_live = True
        # ─── Power-up de disparo infinito ───
        self._infinite_shoot = False
        self._infinite_end_time = 0

        # Lista de frames del soldado
        self._frames = []

        # Cargar hoja de sprites
        sheet_path = Configurations.get_soldier_sheet_path1()
        soldier_sheet = pygame.image.load(sheet_path)

        # Calcular tamaño de cada frame
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_frames_per_column = Configurations.get_frames_per_column()
        sheet_width = soldier_sheet.get_width()
        sheet_height = soldier_sheet.get_height()
        soldier_frame_width = sheet_width // sheet_frames_per_row
        soldier_frame_height = sheet_height // sheet_frames_per_column
        soldier_frame_size = Configurations.get_soldier_size()

        # Recortar y escalar frames
        for i in range(sheet_frames_per_column):
            for j in range(sheet_frames_per_row):
                x = j * soldier_frame_width
                y = i * soldier_frame_height
                subsurface_rect = (x, y, soldier_frame_width, soldier_frame_height)
                frame = soldier_sheet.subsurface(subsurface_rect)
                frame = pygame.transform.scale(frame, soldier_frame_size)
                self._frames.append(frame)

        # Inicializar animación
        self._last_update_time = pygame.time.get_ticks()
        self._frame_index = 0
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Posición en pantalla
        self.rect = self.image.get_rect()
        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right
        self.rect.centery = screen_rect.centery

        # Movimiento vertical
        self._rect_y = float(self.rect.y)
        self._speed = Configurations.get_soldier_speed()

    # ─────────────────────────────────────────────
    # MÉTOD0 EXTRA: Activar power‑up de disparo infinito
    # ─────────────────────────────────────────────
    def activate_infinite_shoot(self, duration_ms: int) -> None:
        """Activa el disparo infinito durante *duration_ms* milisegundos."""
        self._infinite_shoot = True
        self._infinite_end_time = pygame.time.get_ticks() + duration_ms

    # ─────────────────────────────────────────────
    # 2. Movimiento del soldado
    # ─────────────────────────────────────────────
    def update_position(self, screen: pygame.surface.Surface) -> None:
        """
        Actualiza la posición del soldado en pantalla.
        """
        if not self.is_live:
            return

        # ─── Comprobar expiración del power‑up ───
        if self._infinite_shoot and pygame.time.get_ticks() > self._infinite_end_time:
            self._infinite_shoot = False

        screen_rect = screen.get_rect()

        if self._is_moving_up:
            self._rect_y -= self._speed
        elif self._is_moving_down:
            self._rect_y += self._speed

        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.y)
        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())

        self.rect.y = int(self._rect_y)

    # ─────────────────────────────────────────────
    # 3. Animación del soldado
    # ─────────────────────────────────────────────
    def update_animation(self) -> None:
        """
        Actualiza la animación del soldado.
        """
        if not self.is_live:
            return

        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            sheet_frames_per_row = Configurations.get_frames_per_row()

            if not self._is_shooting and self._frame_index >= sheet_frames_per_row or \
               self._is_shooting and self._frame_index >= 2 * sheet_frames_per_row:
                self._frame_index = 0
            elif self._is_shooting and self._frame_index == 1:
                self._is_shooting = False

    # ─────────────────────────────────────────────
    # 4. Disparo del soldado
    # ─────────────────────────────────────────────
    def shoots(self) -> None:
        """
        Indica que el soldado ha disparado.
        """
        self._is_shooting = True
        sheet_frames_per_row = Configurations.get_frames_per_row()
        self._frame_index = sheet_frames_per_row
        self._last_update_time = pygame.time.get_ticks()

    # ─────────────────────────────────────────────
    # 5. Dibujar en pantalla
    # ─────────────────────────────────────────────
    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Dibuja el soldado en pantalla.
        """
        screen.blit(self.image, self.rect)

    # ─────────────────────────────────────────────
    # 6. Getters y Setters
    # ─────────────────────────────────────────────
    @property
    def is_moving_up(self) -> bool:
        return self._is_moving_up

    @is_moving_up.setter
    def is_moving_up(self, value: bool) -> None:
        self._is_moving_up = value

    @property
    def is_moving_down(self) -> bool:
        return self._is_moving_down

    @is_moving_down.setter
    def is_moving_down(self, value: bool) -> None:
        self._is_moving_down = value

    @property
    def is_shooting(self) -> bool:
        return self._is_shooting

    @is_shooting.setter
    def is_shooting(self, value: bool) -> None:
        self._is_shooting = value

    @property
    def is_live(self) -> bool:
        return self._is_live

    @is_live.setter
    def is_live(self, value: bool) -> None:
        self._is_live = value