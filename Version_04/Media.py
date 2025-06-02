# Juan Bautista Juárez
# Fecha: 21 de Mayo de 2025
# Descripción: version 04 Juego del gato
# Media del juego

import pygame
from Configurations import Configurations

class Background:

    """
    Clase que contiene el fondo de pantalla
    """
    def __init__(self):
        """

        """
        background_image_path=Configurations.get_background_image_path()
        self.image=pygame.image.load(background_image_path)

        #Se escala la imagen al tamaño de la pantalla
        screen_size=Configurations.get_screen_size()
        self.image=pygame.transform.scale(self.image,screen_size)

        self.rect = self.image.get_rect()

    def blit (self,screen:pygame.surface.Surface)->None:
        """
        Se utiliza para dibujar el fondo de pantalla
        """
        screen.blit(self.image,self.rect)
