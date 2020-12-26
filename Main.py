import pygame
from pygame import init, display, image, Rect, time, QUIT, MOUSEBUTTONDOWN, draw, Surface, transform
import Play
import Shop

SIZE = WIDTH, HEIGHT = 1920, 1080


class Main:

    def __init__(self):

        init()
        display.set_caption('Sweet House')
        self.screen = display.set_mode(SIZE)

        self.menu_image = image.load("./Data/Pictures/MENU.png")
        self.play_btn_rect = Rect((1220, 475), (220, 100))
        self.shop_btn_rect = Rect((1245, 590), (220, 110))

    def run(self):

        exit_ = False
        clock = time.Clock()

        while not exit_:

            clock.tick(60)

            self.screen.blit(self.menu_image, (0, 0))
            # draw.rect(self.screen, (0, 0, 255), self.play_btn_rect, 1)  # NOTE FOR DEVELOPERS
            # draw.rect(self.screen, (0, 0, 255), Rect((1245, 590), (220, 110)), 1)  # NOTE FOR DEVELOPERS
            display.flip()

            for event in pygame.event.get():

                if event.type == QUIT:
                    exit_ = True

                if event.type == MOUSEBUTTONDOWN:

                    if self.play_btn_rect.collidepoint(event.pos):

                        Play.Play().run()

                    if self.shop_btn_rect.collidepoint(event.pos):

                        Shop.Shop().run()


if __name__ == '__main__':
    Main().run()
