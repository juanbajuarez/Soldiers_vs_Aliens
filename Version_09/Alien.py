from random import uniform

import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from random import choice, uniform, randint

class Alien(Sprite):
    """
    Clase que representa un soldado (personaje principal).
    Hereda de la clase Sprite para utilizar grupos de sprites y detectar colisiones entre sprites.
    Sus atributos son: image (apariencia), rect (posición y tamaño) y banderas de movimiento. Además, tiene una
                       lista con los frames para el movimiento y la animación, así como los atributos requeridos
                       para tal fin.
    Sus métodos son: blit() (dibujar), update_position (para el movimiento), update_animation (para la animación),
                     y getters y setters de las banderas de movimiento.
    """


    def __init__(self, screen:pygame.surface.Surface):
        """
        Constructor del soldado, en donde se llama al constructor padre de Sprite.
        :param screen: Objeto con la pantalla.
        """
        # Se llama al constructor de la clase padre.
        super().__init__()


        # Banderas de movimiento. Inicialmente, el personaje no se mueve.
        movement_bool_value = choice([True,False])
        self._is_moving_up = movement_bool_value
        self._is_moving_down = not movement_bool_value


        # Lista que almacena los frames del soldado.
        self._frames = []


        # Se carga la hoja que contiene los frames del soldado.
        sheet_path = choice(Configurations.get_aliens_Sheets())
        alien_sheet = pygame.image.load(sheet_path)


        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_width = alien_sheet.get_width()
        sheet_height = alien_sheet.get_height()
        alien_frame_width = sheet_width // sheet_frames_per_row
        alien_frame_height = sheet_height


        # Se obtiene el tamaño para escalar cada frame.
        alien_frame_size = Configurations.get_soldier_size()


        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * alien_frame_width
            y = 0
            subsurface_rect = (x, y, alien_frame_width, alien_frame_height)
            frame = alien_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, alien_frame_size)

            self._frames.append(frame)


        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()    # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0                               # Índice de la lista.


        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, a la izquierda de la pantalla.
        screen_rect = screen.get_rect()

        #self.rect.left = screen_rect.left
        self.rect.centery = screen_rect.centery
        self.rect.y = alien_frame_size[1] * randint(0, (screen.get_height() // alien_frame_size[1] - 1))
        self.rect.x = -alien_frame_size[0]

        # Se incluyen los atributos para el movimiento.
        self._rect_y = float(self.rect.y)
        self._rect_x = float(self.rect.x)
        self._speed_x = Configurations.get_alien_speed_x()* uniform(0.8,0.2)
        self._speed_y = Configurations.get_alien_speed_y()*uniform(2.5, 2.0)

        #self.rect.x = apple_size * randint(0, (screen_width // apple_size - 1))





    def update_position(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para actualizar la posición del soldado de acuerdo a las banderas de movimiento.
        :param screen: Pantalla en donde se verifican los límites.
        """


        # Se obtiene el rectángulo del borde de la pantalla
        screen_rect = screen.get_rect()
        self._rect_x += self._speed_x
        self.rect.x = int(self._rect_x)

        # Se verifican los estados de la bandera para modificar la posición.
        if self._is_moving_up:
            self._rect_y -= self._speed_y

        elif self._is_moving_down:
            self._rect_y += self._speed_y

        # Se verifica que el personaje no sobrepase los bordes de la pantalla.
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.y)
            self.is_moving_down = True
            self.is_moving_up = False

        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())
            self.is_moving_down = False
            self.is_moving_up = True

        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.y = int(self._rect_y)


    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frame_delay()
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
    def is_moving_up(self) -> bool:
        """
        Getter para self._is_moving_up.
        """
        return self._is_moving_up

    @is_moving_up.setter
    def is_moving_up(self, value: bool) -> None:
        """
        Setter para self._is_moving_up
        """
        self._is_moving_up = value

    @property
    def is_moving_down(self) -> bool:
        """
        Getter para self._is_moving_down.
        """
        return self._is_moving_down

    @is_moving_down.setter
    def is_moving_down(self, value: bool) -> None:
        """
        Setter para self._is_moving_down
        """
        self._is_moving_down = value