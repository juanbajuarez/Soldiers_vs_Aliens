import pygame
from pygame.sprite import Sprite
from random import randint
from Configurations import Configurations

class PowerUp(Sprite):
    def __init__(self, screen: pygame.surface.Surface):
        super().__init__()

        # Cargar imagen desde ruta y escalar
        image_path = Configurations.get_power_up_image_path()
        power_up_size = Configurations.get_power_up_size()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, power_up_size)

        # Posicionamiento inicial
        self.rect = self.image.get_rect()
        screen_rect = screen.get_rect()
        self.rect.y = power_up_size[1] * randint(0, (screen.get_height() // power_up_size[1] - 1))
        self.rect.x = -power_up_size[0]  # empieza fuera de pantalla a la izquierda

        # Movimiento
        self._rect_x = float(self.rect.x)
        self._rect_y = float(self.rect.y)
        self._speed_x = Configurations.get_power_up_speed()

    def update_position(self, screen: pygame.surface.Surface) -> None:
        self._rect_x += self._speed_x
        self.rect.x = int(self._rect_x)

    def blit(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.image, self.rect)
