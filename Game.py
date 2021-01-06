from random import choice
import pygame
from pygame import init, display, image, Rect, time, QUIT, KEYDOWN, K_SPACE, K_RIGHT, K_LEFT, K_UP, K_DOWN, draw

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

        self.sprite_x = 50
        self.sprite_y = 520

        self.sprite_box = Rect(
            self.sprite_x, self.sprite_y,
            self.sprite_img.get_width(), self.sprite_img.get_height()
        )

        # COLUMNS

        self.column_move = 0

        self.column_width = 90
        self.column_x = 2000
        self.column_y = 0

        self.column_gap_y = 300

        #self.column_gap_list = [choice(range(300, 700, 10)) for i in range(50)]
        self.column_gap_list = [600 for i in range(50)]

        self.column_gap_height = 300
        self.column_gap_size = self.column_width, self.column_gap_height
        self.column_gap_position = self.column_x, self.column_gap_y
        self.column_gap = Rect(self.column_gap_position, self.column_gap_size)

        self.upd_column_height = HEIGHT - (self.column_gap_y + self.column_gap_height)

        self.upd_column_y = self.column_gap_y + self.column_gap_height

        self.column_on_picture_x = 90
        self.upd_column_on_picture_x = 190
        self.column_on_picture_y = 1000

        self.column_on_picture = Rect(
            self.column_on_picture_x, self.column_on_picture_y,
            self.column_width, self.column_gap_y
        )

        self.upd_column_on_picture = Rect(
            self.upd_column_on_picture_x, self.column_on_picture_y,
            self.column_width, self.upd_column_height
        )

        self.column_box = Rect(
            self.column_x, self.column_y,
            self.column_width, self.column_gap_y
        )

        self.upd_column_box = Rect(
            self.column_x, self.upd_column_y,
            self.column_width, self.column_gap_y
        )

        self.boxes_list = []

    def draw(self):

        self.screen.blit(self.bg_picture, (0, 0))
        self.screen.blit(self.sprite_img, (self.sprite_x, self.sprite_y))

        if not self.dead() and self.start:

            self.column_x = 1920

            self.screen.blit(self.columns_picture, (self.column_x - self.column_move, self.column_y), self.column_on_picture)
            self.screen.blit(self.columns_picture, (self.column_x, self.upd_column_y), self.upd_column_on_picture)

            self.infinite_columns()

    def infinite_columns(self):

        for i in range(10):
            self.column_move += 0.1
            self.column_gap_y = self.column_gap_list[i]
            self.draw_column(self.column_gap_y)

    def draw_column(self, i):

        self.update_boxes(i)

        '''if self.column_x - self.column_move > 0:
            self.column_x += 300  # SPACE BETWEEN COLUMNS
        else:
            self.column_move = 0'''

        self.column_x += 300

        self.screen.blit(self.columns_picture, (self.column_x - self.column_move, self.column_y), self.column_on_picture)
        self.screen.blit(self.columns_picture, (self.column_x - self.column_move, self.upd_column_y), self.upd_column_on_picture)

    def dead(self):

        for boxes in self.boxes_list:

            for box in boxes:

                if box.colliderect(self.sprite_box):
                    return True
                if self.sprite_y >= HEIGHT:
                    return True

        return False

    def update_boxes(self, i):

        #self.upd_column_height = HEIGHT - (self.column_gap_y + self.column_gap_height)
        #self.upd_column_y = self.column_gap_y + self.column_gap_height

        self.column_gap_y = i - self.column_gap_height

        self.column_on_picture = Rect(
            self.column_on_picture_x, self.column_on_picture_y,
            self.column_width, self.column_gap_y
        )

        self.upd_column_on_picture = Rect(
            self.upd_column_on_picture_x, self.column_on_picture_y,
            self.column_width, self.upd_column_height
        )

        self.sprite_box = Rect(
            self.sprite_x, self.sprite_y,
            self.sprite_img.get_width(), self.sprite_img.get_height()
        )

        self.column_box = Rect(
            self.column_x - self.column_move, self.column_y,
            self.column_width, self.column_gap_y
        )

        self.upd_column_box = Rect(
            self.column_x - self.column_move, self.upd_column_y,
            self.column_width, self.column_gap_y
        )

        draw.rect(self.screen, (0, 0, 255), self.sprite_box, 1)
        draw.rect(self.screen, (0, 0, 255), self.column_box, 1)
        draw.rect(self.screen, (0, 0, 255), self.upd_column_box, 1)

        if [self.column_box, self.upd_column_box] not in self.boxes_list:
            self.boxes_list.append([self.column_box, self.upd_column_box])

        return [self.column_box, self.upd_column_box]

    def run(self):

        exit_ = False
        clock = time.Clock()

        while not exit_:

            clock.tick(120)
            self.draw()
            display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    exit_ = True

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
