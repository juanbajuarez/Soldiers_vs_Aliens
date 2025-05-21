import pygame
from pygame.sprite import Sprite
from Configurations import Configurations


class Soldier(Sprite):

    """
    Clase que contiene el fondo de pantalla
    """
    def __init__(self,screen:pygame.surface.Surface):
        """

        """
        soldier_image_path=Configurations.get_soldiers_image_path()
        soldier_block_size = Configurations.get_soldiers_block_size()
        self.image = pygame.Surface((soldier_block_size,soldier_block_size))
        self.image=pygame.image.load(soldier_image_path)

        screen_rect = screen.get_rect()

        self.rect=screen.get_rect()
        self.rect.centery=screen_rect.centery
        self.rect.right=screen_rect.right

    def blit (self,screen:pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla
        """
        screen.blit(self.image,self.rect)
