import pygame
from pygame import init, display, image, Rect, time, QUIT, MOUSEBUTTONDOWN, Surface, transform, KEYDOWN, K_RIGHT, K_LEFT

SIZE = WIDTH, HEIGHT = 1920, 1080


class Play:

    def __init__(self):

        init()
        self.screen = display.set_mode(SIZE)

        self.bg_picture = image.load("./Data/Pictures/bg_retrowave.jpg")
        self.sprite = image.load("./Data/Sprites/bee2.png")

        self.sprite_x = 50
        self.sprite_y = 470

    def run(self):

        exit_ = False
        clock = time.Clock()

        while not exit_:
            clock.tick(60)

            self.screen.blit(self.bg_picture, (0, 0))
            self.screen.blit(self.sprite, (self.sprite_x, self.sprite_y))
            display.flip()

            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if event.key == K_RIGHT:

                        self.sprite_x += 10

                    if event.key == K_LEFT:

                        self.sprite_x -= 10
