import webbrowser

import pygame
import Game
import Game_2
import Settings
import Shop
from pygame import init, display, image, Rect, time, QUIT, MOUSEBUTTONDOWN, font, Color, draw

import User

SIZE = WIDTH, HEIGHT = 1920, 1080


class Main:

    def __init__(self):

        init()
        display.set_caption('Flappy Bird')
        self.screen = display.set_mode(SIZE)

        self.menu_image = image.load("./Data/Pictures/Menu_6.png")
        self.settings_image = image.load("./Data/Pictures/Settings.png")

        self.play_btn_rect = Rect((893, 473), (135, 135))
        self.settings_btn_rect = Rect((1810, 50), (40, 40))
        self.shop_btn_rect = Rect((1630, 50), (40, 40))
        self.user_btn_rect = Rect((1720, 50), (40, 40))
        self.logo_btn_rect = Rect((1320, 50), (280, 40))

    def run(self):

        exit_ = False
        clock = time.Clock()

        while not exit_:

            clock.tick(60)

            self.screen.blit(self.menu_image, (0, 0))

            # SHADOW FOR PLAY BTN

            '''
            if self.play_btn_rect.collidepoint(pygame.mouse.get_pos()):
                self.shad_btn_menu_image = image.load("./Data/Pictures/Menu_6_shaddow_btn.png")  # move to __init__
                self.screen.blit(self.shad_btn_menu_image, (0, 0))
            '''

            display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    exit_ = True

                if event.type == MOUSEBUTTONDOWN:

                    if self.logo_btn_rect.collidepoint(event.pos):
                        webbrowser.open('https://github.com/stonedpancake/FlappyBee.git', new=2)

                    if self.play_btn_rect.collidepoint(event.pos):
                        Game_2.Game().run()

                    if self.settings_btn_rect.collidepoint(event.pos):
                        Settings.Settings().run()

                    if self.user_btn_rect.collidepoint(event.pos):
                        User.User().run()

                    if self.shop_btn_rect.collidepoint(event.pos):
                        Shop.Shop().run()



if __name__ == '__main__':
    Main().run()
