import pygame
from pygame import init, display, image, Rect, time, QUIT, MOUSEBUTTONDOWN, Surface, transform, KEYDOWN, K_RIGHT, K_LEFT, K_SPACE, draw

SIZE = WIDTH, HEIGHT = 1920, 1080
SF_SIZE = S_WIDTH, S_HEIGHT = 19200, 2000


class Play:

    def __init__(self):

        init()

        self.main_screen = display.set_mode(SIZE)
        self.surface = Surface(SF_SIZE)

        self.bg_picture = image.load("./Data/Pictures/bg_retrowave.jpg")
        self.sprite_img = image.load("./Data/Sprites/bee2.png")

        self.columns = image.load("./Data/Pictures/Column.png")

        self.column_gap = 120  # self.sprite.get_height()
        self.column_cut = 40  # CHANGES COLUMN GAP POSITION

        self.column_x = 1050
        self.column_y = 0

        self.column_height = 444 + self.column_cut
        self.upd_column_y = self.column_y + self.column_height + self.column_gap

        self.column = Rect(90, 1000, 90, self.column_height)
        self.upd_column = Rect(190, 1000 + self.column_cut, 90, HEIGHT - self.upd_column_y + 10)

        self.sprite_x = 50
        self.sprite_y = 470
        self.sprite_width = self.sprite_img.get_width() - 12
        self.sprite_height = self.sprite_img.get_height() - 12

        self.column_box = Rect(self.column_x, self.column_y, self.column.width, self.column.height)
        self.upd_column_box = Rect(self.column_x, self.upd_column_y, self.upd_column.width, self.upd_column.height)

        self.bg_move = 1920

        # COLUMN AND SPRITES PHYSIC

    def main(self):

        self.surface.blit(self.bg_picture, (self.bg_move, 0))

        self.surface.blit(self.sprite_img, (self.sprite_x, self.sprite_y))
        self.sprite_box = Rect(self.sprite_x + 5, self.sprite_y, self.sprite_width, self.sprite_height)

        self.surface.blit(self.columns, (self.column_x, self.column_y), self.column)
        self.surface.blit(self.columns, (self.column_x, self.upd_column_y), self.upd_column)

        # DRAW BOXES

        draw.rect(self.surface, (0, 0, 255), self.column_box, 1)
        draw.rect(self.surface, (0, 0, 255), self.upd_column_box, 1)
        draw.rect(self.surface, (0, 0, 255), self.sprite_box, 1)

        # DRAW BOXES

        self.main_screen.blit(self.surface, (0, 0))
        display.flip()

    def update_box(self, box):
        if box == 'sprite':
            self.sprite_box = Rect(self.sprite_x, self.sprite_y, self.sprite_width, self.sprite_height)

    def move(self):

        self.update_box('sprite')

        if self.column_box.collidepoint(self.sprite_x + self.sprite_img.get_size()[0], self.sprite_y):
            return False
        if self.sprite_y >= HEIGHT:
            return False
        return True

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

                    if event.key == K_RIGHT and self.move():

                        self.sprite_x += 10
                        self.bg_move -= 100

                    if event.key == K_LEFT and self.move():

                        self.sprite_x -= 10
                        self.bg_move += 100

                    if event.key == K_SPACE:

                        self.sprite_y -= 10

