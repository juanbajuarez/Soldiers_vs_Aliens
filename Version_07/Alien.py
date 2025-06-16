from random import choice
import pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class Alien(Sprite):

    def __init__(self,screen:pygame.surface.Surface):

        super().__init__()

        self._is_moving_alien = True

        # Lista que almacena los frames del soldado.
        self._frames = []
        alien_path=[]
        alien_path.append(Configurations.get_alien_sheet_path())
        alien_path.append(Configurations.get_alien2_sheet_path())
        alien_sheet=pygame.image.load(choice(alien_path))

        """NUEVO."""
        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_width = alien_sheet.get_width()
        sheet_height = alien_sheet.get_height()
        alien_frame_width = sheet_width // sheet_frames_per_row
        alien_frame_height = sheet_height

        # Se obtiene el tamaño para escalar cada frame.
        alien_frame_size = Configurations.get_alien_size()

        for i in range(sheet_frames_per_row):
            x = i * alien_frame_width
            y = 0
            subsurface_rect = (x, y, alien_frame_width, alien_frame_height)
            frame = alien_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, alien_frame_size)

            self._frames.append(frame)
        """NUEVO."""
        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.

        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, a la derecha de la pantalla.
        screen_rect = screen.get_rect()
        self.rect.left = screen_rect.left
        self.rect.centery = screen_rect.centery

        """NUEVO."""
        # Se incluyen los atributos para el movimiento.
        self._rect_x = float(self.rect.x)
        self._speed = Configurations.get_alien_speed()

    def update_position(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para actualizar la posición del soldado de acuerdo a las banderas de movimiento.
        :param screen: Pantalla en donde se verifican los límites.
        """
        # Se obtiene el rectángulo del borde de la pantalla
        screen_rect = screen.get_rect()

        # Se verifican los estados de la bandera para modificar la posición.
        if self._is_moving_alien:
            self._rect_x += self._speed

        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.x = int(self._rect_x)

    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_alien_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            # En caso verdadero, se actualiza el frame por el siguiente en la lista.
            # Además, se actualizan los atributos para resetear el tiempo y actualizar el índice.
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            # Finalmente, se verica si el índice ha recorrido todos los frames para volver al inicio de la lista.
            if self._frame_index >= len(self._frames):
                self._frame_index = 0

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el soldado en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """
        # Se dibuja sobre la pantalla.
        screen.blit(self.image, self.rect)

    @property
    def is_moving_alien(self) -> bool:
        """
        Getter para self._is_moving_down.
        """
        return self._is_moving_alien

    @is_moving_alien.setter
    def is_moving_alien(self, value: bool) -> None:
        """
        Setter para self._is_moving_up
        """
        self._is_moving_alien = value

