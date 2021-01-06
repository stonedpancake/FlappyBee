import sys

import pygame
from pygame import display, font, Color, time
from pygame.constants import *


class Keyboard:

    def __init__(self):

        self.screen = display.set_mode((1920, 1080))
        self.screen.fill((0, 0, 0))
        self.font = font.Font('./Materials/Kingthings Trypewriter 2.ttf', 24)

        self.A = self.font.render('A', True, Color('white'))
        self.B = self.font.render('B', True, Color('white'))
        self.C = self.font.render('C', True, Color('white'))
        self.D = self.font.render('D', True, Color('white'))
        self.E = self.font.render('E', True, Color('white'))
        self.F = self.font.render('F', True, Color('white'))
        self.G = self.font.render('G', True, Color('white'))
        self.H = self.font.render('H', True, Color('white'))
        self.I = self.font.render('I', True, Color('white'))
        self.J = self.font.render('J', True, Color('white'))
        self.K = self.font.render('K', True, Color('white'))
        self.L = self.font.render('L', True, Color('white'))
        self.M = self.font.render('M', True, Color('white'))
        self.N = self.font.render('N', True, Color('white'))
        self.O = self.font.render('O', True, Color('white'))
        self.P = self.font.render('P', True, Color('white'))
        self.Q = self.font.render('Q', True, Color('white'))
        self.R = self.font.render('R', True, Color('white'))
        self.S = self.font.render('S', True, Color('white'))
        self.T = self.font.render('T', True, Color('white'))
        self.U = self.font.render('U', True, Color('white'))
        self.V = self.font.render('V', True, Color('white'))
        self.W = self.font.render('W', True, Color('white'))
        self.X = self.font.render('X', True, Color('white'))
        self.Y = self.font.render('Y', True, Color('white'))
        self.Z = self.font.render('Z', True, Color('white'))

        self.a = self.font.render('a', True, Color('white'))
        self.b = self.font.render('b', True, Color('white'))
        self.c = self.font.render('c', True, Color('white'))
        self.d = self.font.render('d', True, Color('white'))
        self.e = self.font.render('e', True, Color('white'))
        self.f = self.font.render('f', True, Color('white'))
        self.g = self.font.render('g', True, Color('white'))
        self.h = self.font.render('h', True, Color('white'))
        self.i = self.font.render('i', True, Color('white'))
        self.j = self.font.render('j', True, Color('white'))
        self.k = self.font.render('k', True, Color('white'))
        self.l = self.font.render('l', True, Color('white'))
        self.m = self.font.render('m', True, Color('white'))
        self.n = self.font.render('n', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))
        self.p = self.font.render('p', True, Color('white'))
        self.q = self.font.render('q', True, Color('white'))
        self.r = self.font.render('r', True, Color('white'))
        self.s = self.font.render('s', True, Color('white'))
        self.t = self.font.render('t', True, Color('white'))
        self.u = self.font.render('u', True, Color('white'))
        self.v = self.font.render('v', True, Color('white'))
        self.w = self.font.render('w', True, Color('white'))
        self.x = self.font.render('x', True, Color('white'))
        self.y = self.font.render('y', True, Color('white'))
        self.z = self.font.render('z', True, Color('white'))

        self.zero = self.font.render('0', True, Color('white'))
        self.one = self.font.render('1', True, Color('white'))
        self.two = self.font.render('2', True, Color('white'))
        self.three = self.font.render('3', True, Color('white'))
        self.four = self.font.render('4', True, Color('white'))
        self.five = self.font.render('5', True, Color('white'))
        self.six = self.font.render('6', True, Color('white'))
        self.seven = self.font.render('7', True, Color('white'))
        self.eight = self.font.render('8', True, Color('white'))
        self.nine = self.font.render('9', True, Color('white'))

        self.keyboard_x = 900
        self.keyboard_y = 540

    def keyboard(self):

        for event_ in pygame.event.get():

            if event_.type == QUIT:
                return False

            if event_.type == KEYDOWN:

                if event_.type == K_DELETE:
                    sys.exit()

                if event_.type == K_ESCAPE:
                    return False

                if event_.key == KMOD_SHIFT:

                    if event_.key == K_a:
                        self.screen.blit(self.A, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_b:
                        self.screen.blit(self.B, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_c:
                        self.screen.blit(self.C, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_d:
                        self.screen.blit(self.D, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_e:
                        self.screen.blit(self.E, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_f:
                        self.screen.blit(self.F, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_g:
                        self.screen.blit(self.G, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_h:
                        self.screen.blit(self.H, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_i:
                        self.screen.blit(self.I, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_j:
                        self.screen.blit(self.J, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_k:
                        self.screen.blit(self.K, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_l:
                        self.screen.blit(self.L, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_m:
                        self.screen.blit(self.M, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_n:
                        self.screen.blit(self.N, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_o:
                        self.screen.blit(self.O, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_p:
                        self.screen.blit(self.P, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_q:
                        self.screen.blit(self.Q, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_r:
                        self.screen.blit(self.R, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_s:
                        self.screen.blit(self.S, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_t:
                        self.screen.blit(self.T, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_u:
                        self.screen.blit(self.U, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_v:
                        self.screen.blit(self.V, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_w:
                        self.screen.blit(self.W, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_x:
                        self.screen.blit(self.X, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_y:
                        self.screen.blit(self.Y, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_z:
                        self.screen.blit(self.Z, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                else:

                    if event_.key == K_a:
                        self.screen.blit(self.a, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_b:
                        self.screen.blit(self.b, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_c:
                        self.screen.blit(self.c, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_d:
                        self.screen.blit(self.d, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_e:
                        self.screen.blit(self.e, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_f:
                        self.screen.blit(self.f, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_g:
                        self.screen.blit(self.g, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_h:
                        self.screen.blit(self.h, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_i:
                        self.screen.blit(self.i, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_j:
                        self.screen.blit(self.j, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_k:
                        self.screen.blit(self.k, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_l:
                        self.screen.blit(self.l, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_m:
                        self.screen.blit(self.m, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_n:
                        self.screen.blit(self.n, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_o:
                        self.screen.blit(self.o, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_p:
                        self.screen.blit(self.p, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_q:
                        self.screen.blit(self.q, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_r:
                        self.screen.blit(self.r, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_s:
                        self.screen.blit(self.s, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_t:
                        self.screen.blit(self.t, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_u:
                        self.screen.blit(self.u, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_v:
                        self.screen.blit(self.v, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_w:
                        self.screen.blit(self.w, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_x:
                        self.screen.blit(self.x, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_y:
                        self.screen.blit(self.y, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)

                    if event_.key == K_z:
                        self.screen.blit(self.z, (self.keyboard_x, self.keyboard_y))
                        display.flip()
                        time.delay(400)