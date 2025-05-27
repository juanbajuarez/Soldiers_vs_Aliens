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
        self._speed=Configurations.get_soldier_speed()
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

        #Velocidad de movimiento del soldado
        self._speed = Configurations.get_soldier_speed()
        self._rect_y=float(self.rect.y)

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

    def update_position(self,screen):
        if self._is_moving_up:
            self._rect_y-=self._speed
        if self._is_moving_down:
            self._rect_y+=self._speed

        #Revisa los limites de la pantalla
        screen_rect = screen.get_rect()
        if self._rect_y<float(screen_rect.top):
            self._rect_y = float(screen_rect.top)
        if self._rect_y > float(screen_rect.bottom-self.image.get_height()):
            self._rect_y = float(screen_rect.bottom-self.image.get_height())

        self.rect.y=int(self._rect_y)

