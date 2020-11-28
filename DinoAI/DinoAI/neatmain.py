#  Copyright (c) 2020.
#  By Jorn Schampheleer
#  Textures copyrighted by google, extracted from the game by chirag64 (https://github.com/chirag64/t-rex-runner-bot)

import pygame
from DinoAI.DinoAI.GameObjects.ground import Ground
from DinoAI.DinoAI.GameObjects.obstacle_spawner import ObstacleSpawner
from DinoAI.DinoAI.GameObjects.neatdinosaur import NeatDinosaur
import DinoAI.DinoAI.NeatHelpers.visualize
import neat

pygame.init()
WIDTH, HEIGHT = 640, 480
GROUND_HEIGHT = 100
white = 255, 255, 255
black = 0, 0, 0
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
speed_multiplier = 1

FPS = 30


def do_events(speed_multiplier):
    for event in pygame.event.get():  # Check for events
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                speed_multiplier = speed_multiplier % 11 + 1
    return speed_multiplier


def draw(deltatime, score, drawables):
    game_display.fill(black)
    draw_score(game_display, score)
    draw_speed(game_display)
    for drawable in drawables:
        drawable.update(deltatime)
        drawable.draw(game_display)

    pygame.display.update()


def draw_score(display, score):
    font = pygame.font.SysFont(None, 24)
    img = font.render(str(score), True, white)
    display.blit(img, (20, 20))


def draw_evolution_info(display, generation, dinosaurs, best_dinosaur):
    font = pygame.font.SysFont(None, 24)
    img = font.render("Generation: " + str(generation), True, white)
    display.blit(img, (20, 40))
    img = font.render("Alive dinosaurs: " + str(len([dino for dino in dinosaurs if dino.alive])), True, white)
    display.blit(img, (20, 60))
    img = font.render("Best dinosaur: " + str(best_dinosaur.dna), True, white)
    display.blit(img, (20, 80))
    img = font.render("Best score: " + str(best_dinosaur.score), True, white)
    display.blit(img, (20, 100))


def draw_speed(display):
    font = pygame.font.SysFont(None, 24)
    img = font.render("Speed: x" + str(speed_multiplier), True, white)
    display.blit(img, (20, 120))


def main():
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        'config'
    )
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    winner = p.run(eval_genomes, n=5000)
    print(winner)


def eval_genomes(genomes, config):
    idx, genomes = zip(*genomes)
    lastframe = pygame.time.get_ticks()  # Get ticks returns current time in milliseconds
    game_clock = pygame.time.Clock()

    # This is the evolutionary loop
    ground = Ground(HEIGHT, GROUND_HEIGHT)
    obstaclespawner = ObstacleSpawner(WIDTH, HEIGHT - GROUND_HEIGHT)

    alive_dinosaurs = [NeatDinosaur(HEIGHT - GROUND_HEIGHT, genome, config) for genome in genomes]

    # This is the game loop for one generation
    game_loop(game_clock, lastframe, alive_dinosaurs, obstaclespawner, ground)

    for dino in alive_dinosaurs:
        dino.genome.fitness = dino.score


def game_loop(game_clock, lastframe, alive_dinosaurs, obstaclespawner, ground):
    global speed_multiplier
    score = 0
    speed = 100
    # Create copy since we will be changing the array to remove dead dinosaurs
    alive_dinosaurs = alive_dinosaurs[:]
    while len(alive_dinosaurs):
        t = pygame.time.get_ticks()  # Get current time
        deltatime = (t - lastframe) / 1000.0  # Find difference in time and then convert it to seconds
        lastframe = t  # Set lastFrame as the current time for next frame.
        # Do speed_range steps within one frametime, this can increase speed
        for i in range(speed_multiplier):
            score += 1
            obstaclespawner.update(deltatime)

            speed_multiplier = do_events(speed_multiplier)

            # Increase speed over time to make game harder
            if speed < 160 and score % 300 == 0:
                speed += 10
                obstaclespawner.increase_speed(speed)
                ground.increase_speed(speed)

            draw(deltatime, score, alive_dinosaurs + [ground] + obstaclespawner.obstacles)

            for dinosaur in alive_dinosaurs:
                if not dinosaur.alive:
                    continue
                dinosaur.score = score
                gamestate = obstaclespawner.get_next_obstacle_xy(dinosaur)
                if gamestate is not None:
                    [dino.react(gamestate) for dino in alive_dinosaurs]
                if obstaclespawner.is_colliding(dinosaur):
                    dinosaur.alive = False

            alive_dinosaurs = [dino for dino in alive_dinosaurs if dino.alive]
        game_clock.tick(FPS)  # Lock fps to 30

        if score > 20000:
            # Probably found an invincible dino that's going to play forever
            break

    return score, speed


if __name__ == "__main__":
    main()
