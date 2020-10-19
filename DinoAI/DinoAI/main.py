#  Copyright (c) 2020.
#  By Jorn Schampheleer
#  Textures copyrighted by google, extracted from the game by chirag64 (https://github.com/chirag64/t-rex-runner-bot)

import pygame
from dinosaur import Dinosaur
from ground import Ground
from obstacle_spawner import ObstacleSpawner

pygame.init()
GROUND_HEIGHT = 100
white = 255, 255, 255
black = 0, 0, 0


def do_events(jumping):
    for event in pygame.event.get():  # Check for events
        if event.type == pygame.QUIT:
            pygame.quit()  # quits
            quit()
        if event.type == pygame.KEYDOWN:  # If user uses the keyboard
            if event.key == pygame.K_SPACE:  # If that key is space
                jumping = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jumping = False
    return jumping


def draw(deltatime, game_display, drawables):
    game_display.fill(black)

    for drawable in drawables:
        drawable.update(deltatime)
        drawable.draw(game_display)

    pygame.display.update()  # updates the screen


def main():
    # Initialize game
    size = width, height = 640, 480
    game_display = pygame.display.set_mode(size)

    dinosaur = Dinosaur(height - GROUND_HEIGHT)
    ground = Ground(height, GROUND_HEIGHT)
    obstaclespawner = ObstacleSpawner(width, height - GROUND_HEIGHT)

    lastframe = pygame.time.get_ticks()  # Get ticks returns current time in milliseconds
    game_clock = pygame.time.Clock()

    jumping = False

    while True:
        t = pygame.time.get_ticks()  # Get current time
        deltatime = (t - lastframe) / 1000.0  # Find difference in time and then convert it to seconds
        lastframe = t  # Set lastFrame as the current time for next frame.

        obstaclespawner.update(deltatime)
        if obstaclespawner.is_colliding(dinosaur):
            break

        jumping = do_events(jumping)

        if jumping:
            dinosaur.jump()

        draw(deltatime, game_display, [dinosaur, ground] + obstaclespawner.obstacles)
        game_clock.tick(30)  # Lock fps to 30


if __name__ == "__main__":
    main()
