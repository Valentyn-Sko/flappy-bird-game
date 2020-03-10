import time
from random import randint

import pygame

black = (0, 0, 0)
white = (255, 255, 255)
surface_width = 950
surface_height = 500

image_height = 43

start_position_x = 150
start_position_y = 200

pygame.init()
surface = pygame.display.set_mode((surface_width, surface_height), )
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()

img = pygame.image.load('Helicopter.png')

y_move = 3


def helicopter(x, y, image):
    surface.blit(img, (x, y))


def make_text_objs(text, font):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()


def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, white, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, white, [x_block, y_block + gap + block_height, block_width, block_height])


def replay_or_quit():
    time.sleep(0.5)
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key


def main():
    x = start_position_x
    y = start_position_y
    y_move = 3

    x_block_move = 3

    x_block = surface_width
    y_block = 0
    block_width = 75
    block_height = randint(0, surface_height)

    gap = image_height * 2

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -7

        y += y_move
        surface.fill(black)
        blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= x_block_move
        helicopter(x, y, img)

        if y > surface_height or y < 0:
            game_over_func()

        pygame.display.update()
        clock.tick(60)


def msg_surface(text):
    small_text = pygame.font.Font('freesansbold.ttf', 20)
    large_text = pygame.font.Font('freesansbold.ttf', 120)

    title_text_surf, title_text_rect = make_text_objs(text, large_text)
    title_text_rect.center = surface_width / 2, surface_height / 2
    surface.blit(title_text_surf, title_text_rect)

    typ_text_surf, typ_text_rect = make_text_objs('Press any key to continue', small_text)
    typ_text_rect.center = surface_width / 2, ((surface_height / 2) + 100)
    surface.blit(typ_text_surf, typ_text_rect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() is None:
        clock.tick()

    main()


def game_over_func():
    msg_surface('Game over!')


main()
pygame.quit()
quit()
