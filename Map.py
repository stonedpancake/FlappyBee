import pygame
from pygame import init, display, image, sprite


SIZE = WIDTH, HEIGHT = 1920, 1080


class Main:

    def __init__(self):

        init()
        display.set_caption('Sweet House')
        self.screen = display.set_mode(SIZE)

        self.sprites = sprite.Group()
