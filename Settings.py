import pygame
from pygame import init, display, image, Rect, time, QUIT, KEYDOWN, K_SPACE, K_RIGHT, K_LEFT, K_UP, K_DOWN, draw, MOUSEBUTTONDOWN

SIZE = WIDTH, HEIGHT = 1920, 1080


class Settings:

    def __init__(self):

        init()
        self.screen = display.set_mode(SIZE)

        self.menu_image = image.load("./Data/Pictures/Menu_6.png")
        self.settings_image = image.load("./Data/Pictures/Settings_6.png")

        self.quit_btn_rect = Rect(760, 240, 65, 30)

    def run(self):

        exit_ = False
        clock = time.Clock()
        while not exit_:

            clock.tick(60)

            self.screen.blit(self.menu_image, (0, 0))
            self.screen.blit(self.settings_image, (760, 240))

            display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    exit_ = True

                if event.type == MOUSEBUTTONDOWN:

                    if self.quit_btn_rect.collidepoint(event.pos):
                        exit_ = True
