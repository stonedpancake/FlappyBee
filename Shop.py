import pygame
from pygame import init, display, image, Rect, time, QUIT, MOUSEBUTTONDOWN, Surface, transform, KEYDOWN, K_RIGHT, K_LEFT, K_SPACE

SIZE = WIDTH, HEIGHT = 1920, 1080


class Shop:

    def __init__(self):

        init()
        self.screen = display.set_mode(SIZE)

        self.shop_ux = image.load("./Data/Pictures/SHOP.png")

    def run(self):

        exit_ = False
        clock = time.Clock()

        while not exit_:
            clock.tick(60)

            self.screen.blit(self.shop_ux, (0, 0))
            display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    exit_ = True
