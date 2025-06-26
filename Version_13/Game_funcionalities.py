import pygame
from pygame.sprite import Group
from Configurations import Configurations
from Media import Background
from Soldier import Soldier
from Soldier2 import Soldier2
from Shot import Shot
from Alien import Alien
from Score import Score
from AudioManager import AudioManager
from random import randint
from PowerUp import PowerUp

def game_events(soldier: Soldier,
                soldier2: Soldier2,
                shots: Group,
                audio: AudioManager) -> bool:
    game_over = False
    controls = Configurations.get_second_player_controls()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True
            soldier_shots = [s for s in shots if s.owner == soldier]
            if event.key == pygame.K_SPACE and (soldier._infinite_shoot or len(soldier_shots) < 2):
                shots.add(Shot(soldier))
                audio.play_sound('shot')
                soldier.shoots()

            if event.key == controls["move_up"]:
                soldier2.is_moving_up = True
            if event.key == controls["move_down"]:
                soldier2.is_moving_down = True
            soldier2_shots = [s for s in shots if s.owner == soldier2]
            if event.key == controls["shoot"] and (soldier2._infinite_shoot or len(soldier2_shots) < 2):
                shots.add(Shot(soldier2))
                audio.play_sound('shot')
                soldier2.shoots()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False

            if event.key == controls["move_up"]:
                soldier2.is_moving_up = False
            if event.key == controls["move_down"]:
                soldier2.is_moving_down = False

    return game_over

def check_collisions(screen: pygame.Surface,
                     soldier: Soldier,
                     soldier2: Soldier2,
                     shots: Group,
                     aliens: Group,
                     score: Score,
                     audio: AudioManager,
                     powerups: Group) -> bool:
    game_over = False
    screen_rect = screen.get_rect()

    # Colisiones disparo vs alien
    collisions = pygame.sprite.groupcollide(shots, aliens, True, True)
    if collisions:
        audio.play_sound('alien_hit')
        for _ in collisions.values():
            score.increase()

    # Eliminar aliens fuera de pantalla
    for alien in aliens.copy():
        if alien.rect.left > screen_rect.right:
            aliens.remove(alien)

    # Eliminar disparos fuera de pantalla
    for shot in shots.copy():
        if shot.rect.right < screen_rect.left or shot.rect.left > screen_rect.right:
            shots.remove(shot)

    # Colisiones jugador vs alien
    if soldier.is_live and pygame.sprite.spritecollide(soldier, aliens, False):
        soldier.is_live = False
        audio.play_sound('game_over')

    if soldier2.is_live and pygame.sprite.spritecollide(soldier2, aliens, False):
        soldier2.is_live = False
        audio.play_sound('game_over')

    # 🚀 Colisiones jugador vs powerup
    for pu in powerups.copy():
        if soldier.is_live and pu.rect.colliderect(soldier.rect):
            soldier.activate_infinite_shoot(Configurations.get_time_power_up())
            powerups.remove(pu)
        elif soldier2.is_live and pu.rect.colliderect(soldier2.rect):
            soldier2.activate_infinite_shoot(Configurations.get_time_power_up())
            powerups.remove(pu)

    # Fin del juego si ambos jugadores están muertos
    if not soldier.is_live and not soldier2.is_live:
        game_over = True

    # Reposición de aliens
    if len(aliens) <= Configurations.get_min_aliens():
        for _ in range(randint(0, 5)):
            aliens.add(Alien(screen))
    if score.score >= Configurations.get_winner():
        print("¡Victoria! Se eliminaron 100 aliens.")
        return True
    return game_over

def screen_refresh(screen: pygame.Surface,
                   clock: pygame.time.Clock,
                   background: Background,
                   soldier: Soldier,
                   soldier2: Soldier2,
                   shots: Group,
                   aliens: Group,
                   score: Score,
                   powerups: Group) -> None:
    background.blit(screen)

    for pu in powerups:
        pu.update_position(screen)
        pu.blit(screen)

    for shot in shots:
        shot.update_position(screen)
        shot.update_animation()
        shot.blit(screen)

    for alien in aliens:
        alien.update_position(screen)
        alien.update_animation()
        alien.blit(screen)

    if soldier.is_live:
        soldier.update_position(screen)
        soldier.update_animation()
        soldier.blit(screen)

    if soldier2.is_live:
        soldier2.update_position(screen)
        soldier2.update_animation()
        soldier2.blit(screen)

    score.draw(screen)
    pygame.display.flip()
    clock.tick(Configurations.get_fps())

def handle_powerups(screen: pygame.Surface,
                    powerups: Group,
                    last_powerup_time: int,
                    powerup_interval: int) -> int:
    now = pygame.time.get_ticks()

    if not powerups and now - last_powerup_time >= powerup_interval:
        powerups.add(PowerUp(screen))
        return now

    for pu in powerups.copy():
        if pu.rect.left > screen.get_width():
            powerups.remove(pu)

    return last_powerup_time
