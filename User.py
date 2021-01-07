import pygame
from pygame import init, display, image, Rect, time, QUIT

SIZE = WIDTH, HEIGHT = 1920, 1080


class User:

    def __init__(self):

        init()
        self.screen = display.set_mode(SIZE)
        self.shop_image = image.load("./Data/Pictures/SHOP.png")

    def run(self):

        exit_ = False
        clock = time.Clock()

        while not exit_:

            clock.tick(60)

            self.screen.blit(self.shop_image, (0, 0))

            display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    exit_ = True
