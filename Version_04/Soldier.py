import pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class Soldier(Sprite):

    """
    Clase que contiene el fondo de pantalla
    """
    def __init__(self,screen):
        """

        """
        super().__init__()

        soldier_image_path=Configurations.get_soldier_image_path()
        self.image=pygame.image.load(soldier_image_path)
        self.image = pygame.transform.scale(self.image, Configurations.get_solder_size())

        self.rect = self.image.get_rect()

        #Centrar al soldado en y
        screen_rect = screen.get_rect()
        self.rect.centery=screen_rect.centery
        self.rect.left=screen_rect.left

        #Banderas de movimiento
        self._is_moving_up=False
        self._is_moving_down=False

    #metodo de instancia.
    @property
    def is_moving_up(self):
        return self._is_moving_up

    @is_moving_up.setter
    def is_moving_up(self,value):
        self._is_moving_up=value

    @property
    def is_moving_down(self):
        return self._is_moving_down

    @is_moving_down.setter
    def is_moving_down(self,value):
        self._is_moving_down = value



    def blit (self,screen:pygame.surface.Surface):
        """
        Se utiliza para dibujar el soldado en pantalla
        """
        screen.blit(self.image,self.rect)

    def update_position(self):
        if self._is_moving_up:
            self.rect.y-=10
        if self._is_moving_down:
            self.rect.y+=10