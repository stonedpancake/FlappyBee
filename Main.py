import webbrowser

import pygame
import Game
import Settings
import Shop
from pygame import init, display, image, Rect, time, QUIT, MOUSEBUTTONDOWN, font, Color, draw

import User

SIZE = WIDTH, HEIGHT = 1920, 1080


class Main:

    def __init__(self):

        init()
        display.set_caption('Flappy Bee')
        self.screen = display.set_mode(SIZE)
        self.menu_image = image.load("./Data/Pictures/Menu_3.png")
        self.settings_image = image.load("./Data/Pictures/Settings.png")

        self.play_btn_rect = Rect((893, 473), (135, 135))
        self.settings_btn_rect = Rect((1810, 50), (60, 60))
        self.user_btn_rect = Rect((1720, 50), (60, 60))
        self.logo_btn_rect = Rect((1410, 50), (280, 60))

    def run(self):

        exit_ = False
        clock = time.Clock()

        while not exit_:

            clock.tick(60)

            self.screen.blit(self.menu_image, (0, 0))

            display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    exit_ = True

                if event.type == MOUSEBUTTONDOWN:

                    if self.play_btn_rect.collidepoint(event.pos):
                        Game.Game().run()

                    if self.settings_btn_rect.collidepoint(event.pos):
                        Settings.Settings().run()

                    if self.user_btn_rect.collidepoint(event.pos):
                        User.User().run()

                    if self.logo_btn_rect.collidepoint(event.pos):
                        webbrowser.open('https://github.com/stonedpancake/FlappyBee.git', new=2)


if __name__ == '__main__':
    Main().run()
