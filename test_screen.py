import tarfile

import pygame
import math
from random import randint
import sys
vec = pygame.math.Vector2

size = 1300, 900
black = [0, 0, 0]
ballground_image = pygame.image.load("images/123.png")
z = 0

wall1 = pygame.image.load('images/www.png')
eat = pygame.image.load('images/eat1.png')
empty = pygame.image.load('images/empty.png')
chel = pygame.image.load('images/chel.png')
portal = pygame.image.load('images/portal.png')


class Wall:
    def __init__(self, _screen, _wall1, _empty):
        self.screen = _screen
        self.wall = _wall1
        self.empty = _empty


def draw_map(screen, map_data):
    for row_nb, row in enumerate(map_data):
        for col_nb, tile in enumerate(row):
            if tile == '1':
                Image = wall1
            elif tile == '2':
                Image = eat
            elif tile == '0':
                Image = empty
            elif tile == 'p':
                Image = portal
            cart_x = row_nb * 20
            cart_y = col_nb * 20
            iso_x = (cart_x - cart_y)
            iso_y = (cart_x + cart_y) / 2
            centered_x = screen.get_rect().centerx + iso_x - 20
            centered_y = screen.get_rect().centery / 2 + iso_y - 20
            screen.blit(Image, (centered_x, centered_y))


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game')
    pygame.display.flip()

    with open('map_data.txt') as f:
        data = f.readlines()
        map_data = []
        for i in data:
            map_data.append([char for char in i[:-1]])
        print(map_data)

    bi_rect = ballground_image.get_rect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(black)
        screen.blit(ballground_image, bi_rect)
        draw_map(screen, map_data)
        pygame.display.flip()
        pygame.time.wait(100)
    pygame.quit()


if __name__ == '__main__':
    main()
