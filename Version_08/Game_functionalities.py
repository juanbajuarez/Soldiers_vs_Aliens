# Juan Bautista Juárez
# Fecha: 21 de Mayo de 2025
# Descripción: version 05 Juego del gato
# Funcionalidades del juego.

from random import randint
import pygame
from Configurations import Configurations
from Media import Background
from Soldier import Soldier
from Shot import Shot
from Alien import Alien


def game_event(soldier:Soldier, gunshots:pygame.sprite.Group, screen)->bool:
    """
    Función que administra los eventos del juego.
    :return: La bandera del fin del juego
    """
    game_over=False
    # Se verifican los eventos(teclado y ratón) del juego
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                soldier.is_moving_up=True
            if event.key==pygame.K_DOWN:
                soldier.is_moving_down=True
            if event.key == pygame.K_SPACE and len(gunshots)<0:
                shot=Shot(screen,soldier)
                shot._is_moving_shot=True
                gunshots.add(shot)
                soldier.shoots()

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                soldier.is_moving_up=False
            if event.key==pygame.K_DOWN:
                soldier.is_moving_down=False
    #Se regresa la bandera
    return game_over
"""Función para implementar las colisiones"""
def check_collitions(screen:pygame.surface.Surface,soldier:Soldier,
                     shots:pygame.sprite.Group,aliens:pygame.sprite.Group)->bool:
    """

    """

    #Se declara la bandera del fin del juego
    game_over = False


    #Se obtiene el rectangulo
    screen_rect=screen.get_rect()

    #Se revisa las coliciones de los disparos
    aliens_gunshots_collitions=pygame.sprite.groupcollide(shots,aliens,True,True)
    for alien in aliens.copy():
        if alien.rect.left>=screen_rect.right:
            aliens.remove(alien)
    if len(aliens_gunshots_collitions)>=1:
        print("Hola")
    for shot in shots.copy():
        if shot.rect.right<=screen_rect.left:
            aliens.remove(shot)

    soldier_aliens_collitions=pygame.sprite.spritecollide(soldier,aliens,False)
    if len(soldier_aliens_collitions)>=1:
        game_over=True

    if len(aliens)<Configurations.get_min_aliens():
        aliens_to_spawn =randint(0, 8)
        for _ in range(aliens_to_spawn):
            alien = Alien(screen)
            aliens.add(alien)
    """ 
    if head.rect.right > screen_rect.right:
        game_over=True
    if head.rect.top < screen_rect.top:
        game_over=True
    if head.rect.bottom > screen_rect.bottom:
        game_over=True
    if head.rect.left < screen_rect.left:
        game_over=True

    #revisar las colisiones de la cabeza de la serpiente con el cuerpo de la serpiente
    head_body_collision = pygame.sprite.spritecollide(head,snake_body,dokill=False)
    if len(head_body_collision) > 1 :
        game_over=True

    #Se revisa la condición de la cabeza de la serpiente con la manzana
    head_apples_collisions=pygame.sprite.spritecollide(head,apples,dokill=True)
    if len(head_apples_collisions)>0:
        new_snake_block=SnakeBlock()
        new_snake_block.rect.x=snake_body.sprites()[-1].rect.x
        new_snake_block.rect.y=snake_body.sprites()[-1].rect.y
        snake_body.add(new_snake_block)
        new_apple=Apple()
        new_apple.random_position(snake_body)
        apples.add(new_apple)

        # Se reproduce el sonido de que la serpiente ha comido la manzana.
        audio.play_eats_apple_sound()

    scoreboard.update(Apple.get_no_apples()-1)
    """

    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock: pygame.time.Clock,background:Background,soldier:Soldier,shots:pygame.sprite.Group,aliens:pygame.sprite.Group)->None:
    """
    Función que administra los elementos visuales del juego

    """

    # Se dibuja el fondo de la pantalla
    background.blit(screen)
    soldier.update_animation()
    soldier.update_position(screen)
    soldier.blit(screen)
    for alien in aliens.sprites():
        alien.update_position(screen)
        alien.update_animation()
        alien.blit(screen)

    if len(shots.sprites()) > 0:
        for shot in shots.sprites():
            shot.position_shot(screen)
            shot.animation_shot()
    shots.draw(screen)
    # Se actualiza la pantalla
    pygame.display.flip()
    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())