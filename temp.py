import time
from random import randint, randrange

import pygame

black = (0, 0, 0)
white = (255, 255, 255)
sunset = (253, 72, 47)
greenyellow = (184, 255, 0)
orange = (255, 113, 0)
purple = (252, 67, 255)
brightblue = (47, 228, 253)

colorChoices = [sunset, greenyellow, orange, purple, brightblue]

surface_width = 950
surface_height = 500

image_height = 43
image_width = 100

start_position_x = 150
start_position_y = 200

pygame.init()
surface = pygame.display.set_mode((surface_width, surface_height), )
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()

img = pygame.image.load('Helicopter.png')

start_y_move = 5
start_x_block_move = 12


def helicopter(x, y, image):
    surface.blit(img, (x, y))


def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Score:' + str(count), True, white)
    surface.blit(text, [10, 10])


def make_text_objs(text, font):
    text_surface = font.render(text, True, sunset)
    return text_surface, text_surface.get_rect()


def blocks(x_block, y_block, block_width, block_height, gap, colorChoice):

    pygame.draw.rect(surface, colorChoice, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, colorChoice, [x_block, y_block + gap + block_height, block_width, surface_height])


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
    y_move = start_y_move

    x_block_move = start_x_block_move

    x_block = surface_width
    y_block = 0
    block_width = 75
    block_height = randint(0, (surface_height / 2))

    gap = image_height * 3

    game_over = False
    current_score = 0
    block_color = colorChoices[randrange(0, len(colorChoices))]

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
        score(current_score)

        blocks(x_block, y_block, block_width, block_height, gap, block_color)
        x_block -= x_block_move
        helicopter(x, y, img)
        score(current_score)

        if y > surface_height - 40 or y < 0:
            game_over_func()

        if x_block < (-1 * block_width):
            x_block = surface_width
            block_height = randint(0, surface_height / 2)
            block_color = colorChoices[randrange(0, len(colorChoices))]

        if x+image_width > x_block:
            if x < x_block + block_width:
                if y < block_height:
                    if x - image_width < block_width + x_block:
                        game_over_func()

        if x+image_width > x_block:
            if y + image_height > block_height+gap:
                if x < block_width + x_block:
                    game_over_func()

        if x <x_block and x > x_block - x_block_move:
            current_score += 1
            if current_score % 3 == 0:
                x_block_move += 5


        pygame.display.update()
        clock.tick(160)


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
