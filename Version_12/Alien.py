import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from random import choice, uniform, randint

class Alien(Sprite):
    """
    Clase que representa un alien (enemigo del juego).
    Hereda de Sprite para usar colisiones y grupos.
    """

    def __init__(self, screen: pygame.surface.Surface):
        """
        Constructor: Inicializa un alien con animación, posición aleatoria y movimiento automático.
        :param screen: Superficie del juego.
        """
        super().__init__()

        # ────── 1. Movimiento inicial aleatorio (sube o baja) ──────
        movement_bool_value = choice([True, False])
        self._is_moving_up = movement_bool_value
        self._is_moving_down = not movement_bool_value

        # ────── 2. Cargar hoja de sprites aleatoria y cortar frames ──────
        self._frames = []

        sheet_path = choice(Configurations.get_aliens_sheets())
        alien_sheet = pygame.image.load(sheet_path)

        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_width = alien_sheet.get_width()
        sheet_height = alien_sheet.get_height()
        alien_frame_width = sheet_width // sheet_frames_per_row
        alien_frame_height = sheet_height

        alien_frame_size = Configurations.get_soldier_size()  # mismo tamaño que el soldado

        for i in range(sheet_frames_per_row):
            x = i * alien_frame_width
            y = 0
            subsurface_rect = (x, y, alien_frame_width, alien_frame_height)
            frame = alien_sheet.subsurface(subsurface_rect)
            frame = pygame.transform.scale(frame, alien_frame_size)
            self._frames.append(frame)

        # ────── 3. Inicialización de animación ──────
        self._last_update_time = pygame.time.get_ticks()
        self._frame_index = 0
        self.image = self._frames[self._frame_index]
        self._frame_index = 1  # siguiente frame

        # ────── 4. Posicionamiento inicial (fuera del borde izquierdo, vertical aleatoria) ──────
        self.rect = self.image.get_rect()
        screen_rect = screen.get_rect()

        self.rect.y = alien_frame_size[1] * randint(0, (screen.get_height() // alien_frame_size[1] - 1))
        self.rect.x = -alien_frame_size[0]  # inicia fuera de pantalla a la izquierda

        self._rect_y = float(self.rect.y)
        self._rect_x = float(self.rect.x)

        # ────── 5. Velocidades con factor aleatorio ──────
        self._speed_x = Configurations.get_alien_speed_x() * uniform(0.2, 0.8)
        self._speed_y = Configurations.get_alien_speed_y() * uniform(2.0, 2.5)

    # ─────────────────────────────────────────────────────────────────────────────
    # MÉTODOS DE MOVIMIENTO Y ANIMACIÓN
    # ─────────────────────────────────────────────────────────────────────────────

    def update_position(self, screen: pygame.surface.Surface) -> None:
        """
        Actualiza la posición del alien automáticamente en X y Y.
        Rebota en los bordes verticales.
        """
        screen_rect = screen.get_rect()

        # Movimiento horizontal constante
        self._rect_x += self._speed_x
        self.rect.x = int(self._rect_x)

        # Movimiento vertical
        if self._is_moving_up:
            self._rect_y -= self._speed_y
        elif self._is_moving_down:
            self._rect_y += self._speed_y

        # Rebote contra los bordes superior/inferior
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.y)
            self.is_moving_down = True
            self.is_moving_up = False

        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())
            self.is_moving_down = False
            self.is_moving_up = True

        # Actualiza posición final
        self.rect.y = int(self._rect_y)

    def update_animation(self) -> None:
        """
        Avanza al siguiente frame si ha pasado suficiente tiempo.
        """
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            if self._frame_index >= len(self._frames):
                self._frame_index = 0

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Dibuja el alien en la pantalla.
        """
        screen.blit(self.image, self.rect)

    # ─────────────────────────────────────────────────────────────────────────────
    # GETTERS y SETTERS para banderas de movimiento
    # ─────────────────────────────────────────────────────────────────────────────

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
