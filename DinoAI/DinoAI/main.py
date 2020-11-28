#  Copyright (c) 2020.
#  By Jorn Schampheleer
#  Textures copyrighted by google, extracted from the game by chirag64 (https://github.com/chirag64/t-rex-runner-bot)

import pygame
from DinoAI.DinoAI.GameObjects.dinosaur import Dinosaur
from DinoAI.DinoAI.GameObjects.ground import Ground
from DinoAI.DinoAI.GameObjects.obstacle_spawner import ObstacleSpawner

pygame.init()
GROUND_HEIGHT = 100
white = 255, 255, 255
black = 0, 0, 0


def do_events(jumping, crouching):
    for event in pygame.event.get():  # Check for events
        if event.type == pygame.QUIT:
            pygame.quit()  # quits
            quit()
        if event.type == pygame.KEYDOWN:  # If user uses the keyboard
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:  # If that key is space
                jumping = True
            if event.key == pygame.K_DOWN:
                crouching = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                jumping = False
            if event.key == pygame.K_DOWN:
                crouching = False
    return jumping, crouching


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
    crouching = False

    while True:
        t = pygame.time.get_ticks()  # Get current time
        deltatime = (t - lastframe) / 1000.0  # Find difference in time and then convert it to seconds
        lastframe = t  # Set lastFrame as the current time for next frame.

        obstaclespawner.update(deltatime)

        jumping, crouching = do_events(jumping, crouching)

        if jumping:
            dinosaur.jump()
        dinosaur.set_crouch(crouching)

        draw(deltatime, game_display, [dinosaur, ground] + obstaclespawner.obstacles)
        if obstaclespawner.is_colliding(dinosaur):
            break
        game_clock.tick(30)  # Lock fps to 30


if __name__ == "__main__":
    main()
