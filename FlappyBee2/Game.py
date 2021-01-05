import pygame
from pygame import init, display, image, Rect, time, QUIT, KEYDOWN, K_SPACE, K_RIGHT, K_LEFT, K_UP, K_DOWN

SIZE = WIDTH, HEIGHT = 1920, 1080


class Game:

    def __init__(self):

        init()
        self.start = False
        self.screen = display.set_mode(SIZE)

        self.bg_picture = image.load("./Data/Pictures/bg_retrowave.jpg")
        self.columns_picture = image.load("./Data/Pictures/Column.png")
        self.sprite_img = image.load("./Data/Sprites/bee2.png")

        # SPRITE

        self.sprite_x = 200
        self.sprite_y = 450

        self.sprite_box = Rect(
            self.sprite_x, self.sprite_x,
            self.sprite_img.get_width(), self.sprite_img.get_height()
        )

        # COLUMNS

        self.column_width = 90
        self.column_x = 2000
        self.column_y = 0

        self.column_gap_height = 150
        self.column_gap_size = self.column_width, self.column_gap_height
        self.column_gap_position = self.column_gap_x, self.column_gap_y = self.column_x, 500
        self.column_gap = Rect(self.column_gap_position, self.column_gap_size)

        self.column_height = self.column_gap_y
        self.upd_column_height = HEIGHT - (self.column_height + self.column_gap_height)

        self.upd_column_y = self.column_height + self.column_gap_height

        self.column_on_picture_x = 90
        self.upd_column_on_picture_x = 190
        self.column_on_picture_y = 1000

        self.column_on_picture = Rect(
            self.column_on_picture_x, self.column_on_picture_y,
            self.column_width, self.column_height
        )

        self.upd_column_on_picture = Rect(
            self.upd_column_on_picture_x, self.column_on_picture_y,
            self.column_width, self.upd_column_height
        )

        self.column_box = Rect(
            self.column_x, self.column_y,
            self.column_width, self.column_height
        )

        self.upd_column_box = Rect(
            self.column_x, self.upd_column_y,
            self.column_width, self.column_height
        )

    def draw(self):

        self.screen.blit(self.bg_picture, (0, 0))
        self.screen.blit(self.sprite_img, (self.sprite_x, self.sprite_y))
        display.flip()

        if not self.dead() and self.start:

            if self.column_x + self.column_width >= 0:

                self.column_x -= 50

                self.screen.blit(self.columns_picture, (self.column_x, self.column_y), self.column_on_picture)
                self.screen.blit(self.columns_picture, (self.column_x, self.upd_column_y), self.upd_column_on_picture)

                display.flip()

            else:

                self.column_x = 2000

    def dead(self):

        if self.column_box.colliderect(self.sprite_box) or self.upd_column_box.colliderect(self.sprite_box):
            return True
        if self.sprite_y >= HEIGHT:
            return True
        return False

    def run(self):

        exit_ = False
        clock = time.Clock()

        while not exit_:

            for event in pygame.event.get():

                clock.tick(60)
                self.draw()

                if event.type == QUIT:
                    break

                if event.type == KEYDOWN:

                    if event.key == K_SPACE:
                        self.start = True

                    if event.key == K_RIGHT and not self.dead():
                        self.sprite_x += 10

                    if event.key == K_LEFT and not self.dead():
                        self.sprite_x -= 10

                    if event.key == K_UP and not self.dead():
                        self.sprite_y -= 10

                    if event.key == K_DOWN and not self.dead():
                        self.sprite_y += 10
