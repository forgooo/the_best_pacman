import pygame
import math
from random import randint
import sys
from enemys import Red

vec = pygame.math.Vector2
size = 1300, 900
black = [0, 0, 0]
background_image = pygame.image.load("123.png")
wall1 = pygame.image.load('www.png')
eat = pygame.image.load('eat1.png')
empty = pygame.image.load('empty.png')
# chel = pygame.image.load('chel.png')
portal = pygame.image.load('portal.png')
super_eat = pygame.image.load('super_eat.png')
map_data = []
mapYlen = 0
mapXlen = 0


clock = pygame.time.Clock()


class Wall:
    def __init__(self, _screen, _wall1, _empty):
        self.screen = _screen
        self.wall = _wall1
        self.empty = _empty

def limit(w, q1, q2):
	#if w < q1:
	#	w = q1
	#elif w > q2:
	#	w = q2
	return min(max(w, q1), q2)

class Pacman:
    def __init__(self, screen):
        self.walkright = [pygame.image.load('sprite/r1.png').convert_alpha(),
                          pygame.image.load('sprite/r2.png').convert_alpha(),
                          pygame.image.load('sprite/r3.png').convert_alpha()]
        self.walkleft = [pygame.image.load('sprite/l1.png').convert_alpha(),
                         pygame.image.load('sprite/l2.png').convert_alpha(),
                         pygame.image.load('sprite/l3.png').convert_alpha()]
        self.walkup = [pygame.image.load('sprite/u1.png').convert_alpha(),
                       pygame.image.load('sprite/u2.png').convert_alpha(),
                       pygame.image.load('sprite/u3.png').convert_alpha()]
        self.walkdown = [pygame.image.load('sprite/d1.png').convert_alpha(),
                         pygame.image.load('sprite/d2.png').convert_alpha(),
                         pygame.image.load('sprite/d3.png').convert_alpha()]
        self.stand = pygame.image.load('sprite/r1.png').convert_alpha()
        self.stand_rect = self.stand.get_rect(centerx=1300 // 2, bottom=900 - 5)
        self.screen = screen
        self.animcount = 0
        self.x = 650
        self.y = 470
        self.cart_x = 12#len(map_data) // 2
        self.cart_y = 17#len(map_data[0]) // 2
        self.starting_pos = [self.x, self.y]
        self.speedx = 0
        self.speedy = 0
        self.speedXcart = 0
        self.speedYcart = 0
        self.lives = 1
        self.current_score = 0
        self.animcount = 0
        self.facing = 2
        self.frags = 0 # кол съединых призраков

    def events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:# and self.collision(1):
                #  print('w')
                self.speedx = -20
                self.speedy = -10
                self.speedXcart = 0
                self.speedYcart = -1
                self.facing = 1
            if event.key == pygame.K_a:# and self.collision(2):
                #  print('a')
                self.speedx = -20
                self.speedy = 10
                self.speedXcart = -1
                self.speedYcart = 0
                self.facing = 2
            if event.key == pygame.K_d:# and self.collision(4):
                #  print('d')
                self.speedx = 20
                self.speedy = -10
                self.speedXcart = 1
                self.speedYcart = 0
                self.facing = 4
            if event.key == pygame.K_s:# and self.collision(3):
                #  print('s')
                self.speedx = 20
                self.speedy = 10
                self.speedXcart = 0
                self.speedYcart = 1
                self.facing = 3
        if not self.collision(self.facing):
            self.speedx = 0
            self.speedXcart = 0
            self.speedy = 0
            self.speedYcart = 0
        self.x += self.speedx
        self.cart_x += self.speedXcart
        self.y += self.speedy
        self.cart_y += self.speedYcart
        self.draw(self.screen)

    def indNow(self, map_data, x, y):
        for row_nb, row in enumerate(map_data):
            for col_nb, tile in enumerate(row):
                cart_x = row_nb * 20
                cart_y = col_nb * 20
                iso_x = (cart_x - cart_y)
                iso_y = (cart_x + cart_y) / 2
                if x == iso_x and y == iso_y:
                    return map_data[row_nb][col_nb]

    def collision(self, dir):  #направление, верх - 1, против часовой
        if dir == 1 and map_data[limit(self.cart_y - 1, 0, len(map_data) - 1)][limit(self.cart_x, 0, len(map_data[0]) - 1)] != '1':
            print(1)
            return True
        if dir == 2 and map_data[limit(self.cart_y, 0, len(map_data) - 1)][limit(self.cart_x - 1, 0, len(map_data[0]) - 1)] != '1':
            print(2)
            return True
        if dir == 3 and map_data[limit(self.cart_y + 1, 0, len(map_data) - 1)][limit(self.cart_x, 0, len(map_data[0]) - 1)] != '1':
            print(3)
            return True
        if dir == 4 and map_data[limit(self.cart_y, 0, len(map_data) - 1)][limit(self.cart_x + 1, 0, len(map_data[0]) - 1)] != '1':
            print(4)
            return True
        print(5)
        return False

    def collisionWithFood(self, dir):  #направление, верх - 1, против часовой
        if map_data[limit(self.cart_y, 0, len(map_data) - 1)][limit(self.cart_x, 0, len(map_data[0]) - 1)] == '2':
            map_data[limit(self.cart_y, 0, len(map_data) - 1)][limit(self.cart_x, 0, len(map_data[0]) - 1)] = 0
            draw_map(self.screen,map_data)


    def draw(self, screen):
        if self.animcount + 1 >= 10:  # 30
            self.animcount = 0
        if self.facing == 1:
            screen.blit(self.walkleft[self.animcount // 3], (self.x, self.y))  # //5
            self.animcount += 1
        elif self.facing == 3:
            screen.blit(self.walkright[self.animcount // 3], (self.x, self.y))  # //5
            self.animcount += 1
        elif self.facing == 4:
            screen.blit(self.walkup[self.animcount // 3], (self.x, self.y))  # //5
            self.animcount += 1
        elif self.facing == 2:
            screen.blit(self.walkdown[self.animcount // 3], (self.x, self.y))  # //5
            self.animcount += 1
        else:
            screen.blit(self.stand, (self.x, self.y))

    def CountInMap(self,mean):
        M = open("tem.txt", "r")
        data = M.readlines()
        M.close() #
        coun = 0
        # Смотрю сколько mean осталось на карте
        for i in range(len(data)):
            for j in data[i]:
                if j == mean:
                    coun += 1
        return coun

    def die(self, screen):
        tempS = open("NowScor.txt", "w") # Открываю временный файл для записи счёта
        self.stDots = 242 - (242 - self.CountInMap(2)) # Сколько ПРОСТОЙ еды собрал игрок
        self.stSdots = 4 - (4 - self.CountInMap(3)) # Сколько СУПЕР еды собрал игрок
        t = self.stDots * 10 + self.stSdots * 50 + self.frags * 100 # Сколько очков игрок заработл
        tempS.write(str(t))
        tempS.close()
        screen.clear()
        pygame.display.flip()


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
            elif tile == '3':
                Image = super_eat
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
        for i in data:
            map_data.append([char for char in i[:-1]])
        print(map_data)
    mapYlen = len(map_data)
    mapXlen = len(map_data[0])

    pacman = Pacman(screen)
    red = Red(screen)

    bi_rect = background_image.get_rect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill(black)
        screen.blit(background_image, bi_rect)
        draw_map(screen, map_data)
        pacman.events(event)
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()


if __name__ == '__main__':
    main()
