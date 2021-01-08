from random import choice
import pygame
from pygame import init, display, image, Rect, time, QUIT, KEYDOWN, K_SPACE, K_RIGHT, K_LEFT, K_UP, K_DOWN, draw, Color
import GameOver

SIZE = WIDTH, HEIGHT = 1920, 1080


class Game:

    def __init__(self):

        init()
        self.start = False
        self.screen = display.set_mode(SIZE)

        self.color = Color('#ff931e')

        self.sprite_img = image.load("./Data/Sprites/tw_bird_orange.png")
        self.sprite_x, self.sprite_y = 50, 520
        self.sprite_box = self.sprite_img.get_rect()

        self.column_x = 1980
        self.column_height = choice(range(300, 700, 10))
        self.upd_column_y = self.column_height + 100
        self.upd_column_height = HEIGHT - self.upd_column_y
        self.column_rect = Rect(self.column_x, 0, 90, self.column_height)
        self.upd_column_rect = Rect(self.column_x, self.upd_column_y, 90, self.upd_column_height)

    def draw(self):

        self.screen.fill(Color('black'))
        self.screen.blit(self.sprite_img, (self.sprite_x, self.sprite_y))

        if self.start and not self.dead():

            self.sprite_y += 0

            if self.column_x + 90 < 0:

                self.column_x = 1980
                self.update_columns()

            self.screen.blit(self.sprite_img, (self.sprite_x, self.sprite_y))

            self.column_x -= 5

            self.column_rect = Rect(self.column_x, 0, 90, self.column_height)
            self.upd_column_rect = Rect(self.column_x, self.upd_column_y, 90, self.upd_column_height)

            draw.rect(self.screen, self.color, self.column_rect, 0)
            draw.rect(self.screen, self.color, self.upd_column_rect, 0)

        if self.dead():

            GameOver.GameOver().run()

    def update_columns(self):

        self.column_height = choice(range(300, 700, 10))
        self.upd_column_y = self.column_height + 100
        self.upd_column_height = HEIGHT - self.upd_column_y

    def dead(self):

        if self.column_rect.colliderect(self.sprite_box) or self.upd_column_rect.colliderect(self.sprite_box):
            return True
        if self.sprite_y >= HEIGHT:
            return True
        return False

    def run(self):

        exit_ = False
        clock = time.Clock()

        while not exit_:

            clock.tick(60)
            self.draw()
            display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    exit_ = True

                if event.type == KEYDOWN:

                    if event.key == K_SPACE:

                        self.start = True

                        if self.start:

                            self.sprite_y -= 5
