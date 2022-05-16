import pygame
from pygame.locals import *
import os
from Rook import *
from Bishop import *
class Queen(pygame.sprite.Sprite):
    def __init__(self, x, y, c):
        super().__init__()
        self.image = pygame.image.load(os.path.join('Images', 'black queen.jpg'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.c = c
        self.player_color(self.c)
        self.click = False
        self.coord = (0, 0)

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def player_color(self, s):
        if s == 'b':
            self.image = pygame.image.load(os.path.join('Images', 'black queen.jpg'))
        elif s == 'w':
            self.image = pygame.image.load(os.path.join('Images', 'white queen.jpg'))

    def move(self, x, y):
        if self.click:
            if self.valid_move(x, y):
                self.rect.x = x
                self.rect.y = y

    def location(self):
        return self.x, self.y

    def valid_move(self, x_pos, y_pos):
        if Bishop.valid_move(x_pos, y_pos) or Rook.valid_move(x_pos, y_pos):
            return True
        else:
            return False

    def is_clicked(self, cor):
        self.coord = cor
        if cor[0] >= self.rect.x and cor[0] <= self.rect.x + 23:
            if cor[1] >= self.rect.y and cor[1] <= self.rect.y + 52:
                self.click = True
                return True
        else:
            self.click = False
            return False

    def type(self):
        return 'queen'
