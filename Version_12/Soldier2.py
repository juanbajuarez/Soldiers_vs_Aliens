import pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class Soldier2(Sprite):
    """
    Segundo personaje jugable con controles alternativos.
    """

    # ─────────────────────────────────────────────
    # 1. Constructor
    # ─────────────────────────────────────────────
    def __init__(self, screen: pygame.Surface):
        """
        Inicializa el segundo soldado con sus atributos, animaciones y posición.
        """
        super().__init__()

        # Banderas de estado
        self._is_moving_up = False
        self._is_moving_down = False
        self._is_shooting = False
        self._is_live = True

        # Lista de frames
        self._frames = []

        # Cargar hoja de sprites
        sheet_path = Configurations.get_soldier_sheet_path()
        soldier_sheet = pygame.image.load(sheet_path)

        # Configuración de recorte de frames
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_frames_per_column = Configurations.get_frames_per_column()
        sheet_width = soldier_sheet.get_width()
        sheet_height = soldier_sheet.get_height()
        frame_width = sheet_width // sheet_frames_per_row
        frame_height = sheet_height // sheet_frames_per_column
        soldier2_size = Configurations.get_soldier2_size()

        # Recortar y escalar cada frame
        for i in range(sheet_frames_per_column):
            for j in range(sheet_frames_per_row):
                x = j * frame_width
                y = i * frame_height
                subsurface_rect = (x, y, frame_width, frame_height)
                frame = soldier_sheet.subsurface(subsurface_rect)
                frame = pygame.transform.scale(frame, soldier2_size)
                self._frames.append(frame)

        # Imagen inicial y rectángulo
        self.image = self._frames[0]
        self.rect = self.image.get_rect()
        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right
        self.rect.centery = screen_rect.centery

        # Movimiento
        self._rect_y = float(self.rect.y)
        self._speed = Configurations.get_soldier_speed()
        self._last_update_time = pygame.time.get_ticks()
        self._frame_index = 0

    # ─────────────────────────────────────────────
    # 2. Movimiento vertical
    # ─────────────────────────────────────────────
    def update_position(self, screen: pygame.Surface) -> None:
        """
        Actualiza la posición vertical según banderas de movimiento.
        """
        if not self.is_live:
            return

        screen_rect = screen.get_rect()

        if self._is_moving_up:
            self._rect_y -= self._speed
        elif self._is_moving_down:
            self._rect_y += self._speed

        # Limitar movimiento a los bordes
        if self._rect_y < screen_rect.top:
            self._rect_y = float(screen_rect.top)
        elif self._rect_y > screen_rect.bottom - self.rect.height:
            self._rect_y = float(screen_rect.bottom - self.rect.height)

        self.rect.y = int(self._rect_y)

    # ─────────────────────────────────────────────
    # 3. Animación del personaje
    # ─────────────────────────────────────────────
    def update_animation(self) -> None:
        """
        Actualiza el frame de animación del personaje según el estado.
        """
        if not self.is_live:
            return

        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frame_delay()

        if (current_time - self._last_update_time) >= frame_delay:
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            frames_per_row = Configurations.get_frames_per_row()

            # Animación en estado normal o de disparo
            if not self._is_shooting and self._frame_index >= frames_per_row:
                self._frame_index = 0
            elif self._is_shooting and self._frame_index >= 2 * frames_per_row:
                self._frame_index = frames_per_row
            elif self._is_shooting and self._frame_index == frames_per_row + 1:
                self._is_shooting = False

    # ─────────────────────────────────────────────
    # 4. Acción de disparo
    # ─────────────────────────────────────────────
    def shoots(self) -> None:
        """
        Activa el estado de disparo y ajusta la animación.
        """
        self._is_shooting = True
        self._frame_index = Configurations.get_frames_per_row()
        self._last_update_time = pygame.time.get_ticks()

    # ─────────────────────────────────────────────
    # 5. Dibujar en pantalla
    # ─────────────────────────────────────────────
    def blit(self, screen: pygame.Surface) -> None:
        """
        Dibuja el personaje en la pantalla.
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
