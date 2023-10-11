import pygame

map_data = []


class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.x = 0   # начальные точки создания ПОМЕНЯТЬ НА НУЖНЫЕ
        self.y = 0   # начальные точки создания ПОМЕНЯТЬ НА НУЖНЫЕ
        self.dir = 2   # направление от 1 до 4, изначально смотрит налево
        self.targetX = 0
        self.targetY = 0
        self.cornerXY = [0, 0]

        self.speedX = 20
        self.speedY = 10
        # Размеры
        self.width = 30  # ширина ПОМЕНЯТЬ НА НУЖНЫЕ
        self.height = 60  # высота ПОМЕНЯТЬ НА НУЖНЫЕ
        # Параметры спрайта
        self.spryte = pygame.image.load('stand1.png').convert_alpha()  # Загрузка спрайта
        self.spryte = pygame.transform.scale(self.spryte, (self.width, self.height))  # Подгон под размеры
        self.chbox = pygame.rect(screen, (self.x, self.y - 60, 30, 60))  # Создание CheckBox для кализии
        # Параметры статуса
        self.fear = 0  # Страх - опредиляет догоняет ли враг или убегает
        # False - догоняет
        # True - убегает
        self.status = "stand1"  # Определяет каое состояние + спрайт
        self.speed = 20  # Скорость перемещение

        with open('map_data.txt') as f:
            data = f.readlines()
            for i in data:
                map_data.append([char for char in i[:-1]])
            print(map_data)

        self.draw()

    def move(self):  # подвинуться на соседнюю клетку в сторону self.dir
        if self.dir == 1:
            self.y += self.speedY
        elif self.dir == 2:
            self.x -= self.speedX
        elif self.dir == 3:
            self.y -= self.speedY
        elif self.dir == 4:
            self.x += self.speedX

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

    def follow(self):  # с помощью self.dir идти к клетке
        dist = ((self.x - self.targetX) ** 2 + (self.y - self.targetY) ** 2) ** (1 / 2)
        if dist < ((self.x - self.targetX) ** 2 + (self.y - 1 - self.targetY) ** 2) ** (
                1 / 2) and dir != 3 and self.colllision(1):
            dir = 1
        elif dist < ((self.x - 1 - self.targetX) ** 2 + (self.y - self.targetY) ** 2) ** (
                1 / 2) and dir != 4 and self.colllision(2):
            dir = 2
        elif dist < ((self.x - self.targetX) ** 2 + (self.y + 1 - self.targetY) ** 2) ** (
                1 / 2) and dir != 1 and self.colllision(3):
            dir = 3
        elif dist < ((self.x + 1 - self.targetX) ** 2 + (self.y - self.targetY) ** 2) ** (
                1 / 2) and dir != 2 and self.colllision(4):
            dir = 4


def change_target(self, Px, Py, dir): # у каждого индивидуально
        pass


def fear_run(self):
    targetX = randint(0, 28)
    targetY = randint(0, 31)

    def draw(self):
        if self.status.find("stoit") != -1:  # Определяет состояние, если стоит то True

            if self.fear == 0 or 1:  # Проверка на страх врага

                # Подгатовка ОБЫЧНОГО спрайта ПОКОЯ

                self.spryte = pygame.image.load('stoit1.png').convert_alpha()



            else:

                # Подгатовка В СТРАХЕ спрайта ПОКОЯ

                pass
        else:
            if self.fear == 0:  # Проверка на страх врага

                # Подгатовка ОБЫЧНОГО спрайта ПЕРЕМЕЩЕНИЕ

                if self.status.find(".1") != -1: #вверх
                    if self.status.find("1.") != -1:
                        self.spryte = pygame.image.load('1.1.png').convert_alpha()
                        self.status = "2.1"

                    elif self.status.find("2.") != -1:
                        self.spryte = pygame.image.load('2.1.png').convert_alpha()
                        self.status = "3.1"

                    elif self.status.find("3.") != -1:
                        self.spryte = pygame.image.load('3.1.png').convert_alpha()
                        self.status = "4.1"

                    elif self.status.find("4.") != -1:
                        self.spryte = pygame.image.load('4.1.png').convert_alpha()
                        self.status = "5.1"

                    elif self.status.find("5.") != -1:
                        self.spryte = pygame.image.load('5.1.png').convert_alpha()
                        self.status = "6.1"

                    elif self.status.find("6.") != -1:
                        self.spryte = pygame.image.load('6.1.png').convert_alpha()
                        self.status = "1.1"

                elif self.status.find(".2") != -1: #влево

                    if self.status.find("1.") != -1:

                        self.spryte = pygame.image.load('1.2.png').convert_alpha()

                        self.status = "2.2"


                    elif self.status.find("2.") != -1:

                        self.spryte = pygame.image.load('2.2.png').convert_alpha()

                        self.status = "3.2"


                    elif self.status.find("3.") != -1:

                        self.spryte = pygame.image.load('3.2.png').convert_alpha()

                        self.status = "4.2"


                    elif self.status.find("4.") != -1:

                        self.spryte = pygame.image.load('4.2.png').convert_alpha()

                        self.status = "5.2"


                    elif self.status.find("5.") != -1:

                        self.spryte = pygame.image.load('5.2.png').convert_alpha()

                        self.status = "6.2"


                    elif self.status.find("6.") != -1:

                        self.spryte = pygame.image.load('6.2.png').convert_alpha()

                        self.status = "1.2"

                elif self.status.find(".3") != -1:#вправо

                    if self.status.find("1.") != -1:

                        self.spryte = pygame.image.load('1.3.png').convert_alpha()

                        self.status = "2.3"


                    elif self.status.find("2.") != -1:

                        self.spryte = pygame.image.load('2.3.png').convert_alpha()

                        self.status = "3.3"


                    elif self.status.find("3.") != -1:

                        self.spryte = pygame.image.load('3.3.png').convert_alpha()

                        self.status = "4.3"


                    elif self.status.find("4.") != -1:

                        self.spryte = pygame.image.load('4.3.png').convert_alpha()

                        self.status = "5.3"


                    elif self.status.find("5.") != -1:

                        self.spryte = pygame.image.load('5.3.png').convert_alpha()

                        self.status = "6.3"


                    elif self.status.find("6.") != -1:

                        self.spryte = pygame.image.load('6.3.png').convert_alpha()

                        self.status = "1.3"

                else:#Вниз

                    if self.status.find("1.") != -1:

                        self.spryte = pygame.image.load('1.4.png').convert_alpha()

                        self.status = "2.4"


                    elif self.status.find("2.") != -1:

                        self.spryte = pygame.image.load('2.4.png').convert_alpha()

                        self.status = "3.4"


                    elif self.status.find("3.") != -1:

                        self.spryte = pygame.image.load('3.4.png').convert_alpha()

                        self.status = "4.4"


                    elif self.status.find("4.") != -1:

                        self.spryte = pygame.image.load('4.4.png').convert_alpha()

                        self.status = "5.4"


                    elif self.status.find("5.") != -1:

                        self.spryte = pygame.image.load('5.4.png').convert_alpha()

                        self.status = "6.4"


                    elif self.status.find("6.") != -1:

                        self.spryte = pygame.image.load('6.4.png').convert_alpha()

                        self.status = "1.4"

            else:
                pass

    def update(self, player, fear = 0):
        self.change_target(player.x, player.y, player.facing)
        if fear:
            self.fear == 1
        if self.fear == 1:
            fear_run()
        elif self.fear == 0:
            targetX = cornerXY[0]
            targetY = cornerXY[1]
        self.follow()
        self.move()
        if ((player.x - self.x)**2 + (player.y == self.y)**2)**(1/2) <= 1:
            player.die()


class Red(Enemy):
    def __init__(self, screen):
        super.__init__(screen)
        cornerXY = [500, 0]
    def change_target(self, Px, Py, dir):
        self.targetX = Px, self.targetY = Py


class Pink(Enemy):
    def __init__(self):
        super.__init__()
        cornerXY = [0, 0]
    def change_target(self, Px, Py, dir):
        self.target = Px , Py
        if dir == 3 and self.targetY - 80 > 0:
            self.target[1] -= 80

        if dir == 2 and self.targetX - 80 > 0:
            self.target[0] -= 80

        if dir == 1 and self.targetY + 80 < 512:
            self.target[1] += 80

        if dir == 4 and self.targetX + 80 < 521:
            self.target[0] += 80


class Blue(Enemy):
    def __init__(self):
        super.__init__()
        cornerXY = [0, 500]
    def change_target(self, Px, Py, dir, Rx, Ry):
        if dir == 1:
            Py += 2
        elif dir == 2:
            Px -= 2
        elif dir == 3:
            Py -= 2
        elif dir == 4:
            Px += 2
        self.targetX = (Px - Rx) * 2 + Px
        self.targetY = (Py - Ry) * 2 + Py


class Orange(Enemy):
    def __init__(self):
        super.__init__()
        cornerXY = [500, 500]

    def OrDistence(self,Px, Py):
        if ((Px-self.x)**2+(Py-self.y)**2)**0.5 > 30:
            return False
        return True

    def change_target(self, Px, Py, dir):
        if self.OrDistence(Px, Py):
            self.targetX, self.targetY = Px , Py
        else:
            self.targetX, self.targetY = self.targetX * -1, self.targetY * -1
