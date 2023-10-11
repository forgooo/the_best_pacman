import pygame
import pygame_menu
import sys
from pygame_menu import Theme
from sys import path

black = [0, 0, 0]
size = 1300, 900

'''class Menu:
    def __init__(self):
        self.first_frase = 'Play'
        self.second_frase = 'Leaderboard'
        self.third_frase = 'Settings'

    def draw_menu(self):
        pass'''


def terminate():
    pygame.quit()
    sys.exit()


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game')
    pygame.display.flip()

    # MENU
    cus = Theme(widget_font=pygame_menu.font.FONT_8BIT, background_color=(0, 0, 0, 0))
    menu = pygame_menu.Menu('Welcum', 1300, 900,
                            theme=cus)
    menu.add.text_input('Name :', default='Slave')
    menu.add.button('Play', None)  # Заменить None игру
    menu.add.button('Quit', None)

    # SOUND
    # sound_dir = path.join(path.dirname(__file__), 'sounds')
    pygame.mixer.init()
    '''main_theme = pygame.mixer.Sound(path.join(sound_dir, 'sounds/main_theme.ogg'))
    click = pygame.mixer.Sound(path.join(sound_dir, 'sounds/woo.ogg'))
    main_theme.set_volume(0.1)
    click.set_volume(0.3)'''
    main_theme = pygame.mixer.Sound('sounds/main_theme.ogg')
    click = pygame.mixer.Sound('sounds/woo.ogg')
    main_theme.set_volume(0.1)
    click.set_volume(0.3)

    running = True
    flag = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.mixer.music.fadeout(1500)
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_theme.set_volume(0.02)
                click.play()
        main_theme.set_volume(0.1)
        screen.fill(black)
        if menu.is_enabled():
            menu.draw(screen)
            if flag:
                main_theme.play()
                flag = 0
        print('thank u sir')
        pygame.display.flip()
        pygame.time.wait(100)
    pygame.quit()


if __name__ == '__main__':
    main()
