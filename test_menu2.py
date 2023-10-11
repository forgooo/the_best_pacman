import abc
import os
import pygame

pygame.init()
pygame.font.init()

RUNNING = True


def play(**kwargs):
    try:
        os.system('python3 main.py')
    except:
        ('хз что произошло')


class MenuElement(abc.ABC):
    def __init__(self, x, y, size, content, func_handler):
        self.w, self.h = size
        self._x, self._y = x, y
        self.content = content
        self.rect = pygame.Rect(self._x, self._y, self.w, self.h)
        self.func_handler = func_handler

    @property
    @abc.abstractmethod
    def loc(self):
        pass

    @abc.abstractmethod
    def draw(self, screen):
        pass

    def update(self, **kwargs):
        if self.func_handler is not None:
            self.func_handler(**kwargs)


class Button(MenuElement):
    def __init__(self, size, content, func_handler, font_weight):
        super().__init__(0, 0, size, content, func_handler)

        self.highlight = False
        self.font_weight = font_weight
        self.font = pygame.font.SysFont('Comic Sans MS', font_weight)

    @property
    def loc(self):
        return (self._x, self._y)

    @loc.setter
    def loc(self, value):
        self._x = value[0]
        self._y = value[1]

        self.rect.center = (self._x, self._y)

    def draw(self, screen):
        content = self.font.render(self.content, False, (255, 255, 255))
        content_rect = content.get_rect(center=(self._x, self._y))

        pygame.draw.rect(screen, (100, 100, 100), self.rect, 1 if not self.highlight else 0, 4)
        screen.blit(content, content_rect)


class Menu:
    def __init__(self, wnd_size, elem_size):
        self.wnd_width, self.wnd_height = wnd_size
        self.elem_width, self.elem_height = elem_size
        self.elements = []
        self.selected = -1
        self.hover = -1
        self.checked = False

    def __update_elements(self):
        step = (self.wnd_height - self.elem_height * len(self.elements)) // (len(self.elements) + 1)
        top = step

        for elem in self.elements:
            elem.loc = (self.wnd_width // 2, top + self.elem_height // 2)
            top += (step + self.elem_height)

    def add_elem(self, elem):
        self.elements.append(elem)
        self.__update_elements()

    def draw(self, screen):
        for elem in self.elements:
            elem.draw(screen)

    def update(self):
        for i, elem in enumerate(self.elements):
            elem.highlight = False
            if elem.rect.collidepoint(pygame.mouse.get_pos()):
                elem.highlight = True
                self.hover = i

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected = self.hover

        if self.selected != -1:
            self.elements[self.selected].update()
            self.selected = -1

        self.hover = -1


def close(**kwargs):
    global RUNNING
    RUNNING = False


if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 600))
    wnd_size = (800, 600)
    elem_size = (200, 50)

    menu = Menu(wnd_size, elem_size)
    button = Button(elem_size, "Play", play, 32)
    button1 = Button(elem_size, "Liderboard", None, 32)
    button2 = Button(elem_size, "Exit", close, 32)
    menu.add_elem(button)
    menu.add_elem(button1)
    menu.add_elem(button2)

    clock = pygame.time.Clock()
    while RUNNING:
        screen.fill((0, 0, 0))
        menu.update()
        menu.draw(screen)
        pygame.display.flip()
        clock.tick(30)
