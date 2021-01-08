import pygame
from pygame import init, display, image, Rect, time, QUIT, MOUSEBUTTONDOWN, draw

import Game_2
import Main
import Shop

SIZE = WIDTH, HEIGHT = 1920, 1080


class GameOver:

    def __init__(self):

        init()
        self.screen = display.set_mode(SIZE)
        self.game_over_image = image.load("./Data/Pictures/gameover_violet.png")

        self.home_btn = Rect(875, 540, 40, 40)
        self.play_btn = Rect(940, 540, 40, 40)
        self.shop_btn = Rect(1005, 540, 40, 40)

    def run(self):

        exit_ = False
        clock = time.Clock()

        while not exit_:

            clock.tick(60)
            self.screen.blit(self.game_over_image, (810, 465))
            display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    exit_ = True

                if event.type == MOUSEBUTTONDOWN:

                    if self.home_btn.collidepoint(event.pos):
                        Main.Main().run()

                    if self.play_btn.collidepoint(event.pos):
                        Game_2.Game().run()

                    if self.shop_btn.collidepoint(event.pos):
                        Shop.Shop().run()
