import pygame
from pygame import init, display, image, Rect, time, QUIT, MOUSEBUTTONDOWN, Surface, transform, KEYDOWN, K_RIGHT, K_LEFT, K_SPACE

SIZE = WIDTH, HEIGHT = 1920, 1080


class Play:

    def __init__(self):

        init()
        self.screen = display.set_mode(SIZE)

        self.bg_picture = image.load("./Data/Pictures/bg_retrowave.jpg")
        self.sprite = image.load("./Data/Sprites/bee2.png")

        self.columns = image.load("./Data/Pictures/Column.png")

        # self.sprite.get_height()

        self.column_gap = 90
        self.column_cut = 40  # CHANGES COLUMN GAP POSITION

        self.column_height = 500 + self.column_cut
        self.upd_column_height = 710

        self.column_x = 1050
        self.column_y = 10
        self.upd_column_y = self.column_y + self.column_height + self.column_gap

        self.column = (90, 10, 90, self.column_height)
        self.upd_column = (190, 1000 + self.column_cut, 90, HEIGHT - self.upd_column_y - 10)

        self.sprite_x = 50
        self.sprite_y = 470

    def main(self):

        self.screen.blit(self.bg_picture, (0, 0))
        self.screen.blit(self.sprite, (self.sprite_x, self.sprite_y))

        self.screen.blit(self.columns, (self.column_x, self.column_y), self.column)
        self.screen.blit(self.columns, (self.column_x, self.upd_column_y), self.upd_column)
        display.flip()

    def run(self):

        exit_ = False
        clock = time.Clock()

        while not exit_:
            clock.tick(60)

            self.main()
            display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    exit_ = True

                if event.type == KEYDOWN:

                    if event.key == K_RIGHT:

                        self.sprite_x += 10

                    if event.key == K_LEFT:

                        self.sprite_x -= 10

                    if event.key == K_SPACE:

                        self.sprite_y -= 10

