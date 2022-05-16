import pygame
from pygame.locals import *
import os
class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y, c):
        super().__init__()
        self.image = pygame.image.load(os.path.join('Images', 'black knight.jpg'))
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
            self.image = pygame.image.load(os.path.join('Images', 'black knight.jpg'))
        elif s == 'w':
            self.image = pygame.image.load(os.path.join('Images', 'white knight.jpg'))

    def move(self, x, y):
        if self.click:
            if self.valid_move(x, y):
                self.rect.x = x
                self.rect.y = y

    def location(self):
        return self.x, self.y

    def valid_move(self, x_pos, y_pos):
        if y_pos >= self.rect.y - self.rect.height - 60 and y_pos <= self.rect.y - 60:
            if x_pos >= self.rect.x - self.rect.width - 130 and x_pos <= self.rect.x - 130:
                return True
            elif x_pos <= self.rect.x + self.rect.width + 130 and x_pos >= self.rect.x + 130:
                return True
        elif y_pos <= self.rect.y + self.rect.height + 60 and y_pos >= self.rect.x + 60:
            if x_pos >= self.rect.x - self.rect.width - 130 and x_pos <= self.rect.x - 130:
                return True
            elif x_pos <= self.rect.x + self.rect.width + 130 and x_pos >= self.rect.x + 130:
                return True
        elif y_pos >= self.rect.y - self.rect.height - 130 and y_pos <= self.rect.y - 130:
            if x_pos >= self.rect.x - self.rect.width - 60 and x_pos <= self.rect.x - 60:
                return True
            elif x_pos <= self.rect.x + self.rect.width + 60 and x_pos >= self.rect.x + 60:
                return True
        elif y_pos <= self.rect.y + self.rect.height + 103 and y_pos >= self.rect.x + 130:
            if x_pos >= self.rect.x - self.rect.width - 60 and x_pos <= self.rect.x - 60:
                return True
            elif x_pos <= self.rect.x + self.rect.width + 60 and x_pos >= self.rect.x + 60:
                return True
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
        return 'knight'
