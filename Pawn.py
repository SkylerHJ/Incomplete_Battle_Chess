import pygame
from pygame.locals import *
import os
from BlackPlayer import *
from WhitePlayer import *
class Pawn(pygame.sprite.Sprite):
    def __init__(self, x, y, c):
        super().__init__()
        self.image = pygame.image.load(os.path.join('Images', 'black pawn.jpg'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.c = c
        self.player_color(self.c)
        self.click = False
        self.first = True

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def player_color(self, s):
        if s == 'b':
            self.image = pygame.image.load(os.path.join('Images', 'black pawn.jpg'))
        elif s == 'w':
            self.image = pygame.image.load(os.path.join('Images', 'white pawn.jpg'))

    def move(self, x, y):
        if self.click:
            if self.valid_move(x, y):
                self.rect.x = x
                self.rect.y = y
            self.en_passe()
            self.capture()
            self.first = False

    def location(self):
        return self.x, self.y

    def capture(self):
        '''
        for piece in BlackPlayer.black_pieces:
            if piece.location[0] <= self.rect.x + self.rect.width + 60 and piece.location[0] >= self.rect.x + 60:
                if piece.location[1] <= self.rect.y + self.rect.height + 60 and piece.location[1] >= self.rect.y + 60:
                    self.rect.x = location[0]
                    self.rect.y = location[1]
                    piece.rect.x = 700
                    piece.rect.y = 80
            elif piece.location[0] <= self.rect.x - self.rect.width - 60 and piece.location[0] >= self.rect.x +- 60:
                if piece.location[1] <= self.rect.y + self.rect.height + 60 and piece.location[1] >= self.rect.y + 60:
                    self.rect.x = location[0]
                    self.rect.y = location[1]
                    piece.rect.x = 700
                    piece.rect.y = 80
        for piece in WhitePlayer.white_pieces:
            if piece.location[0] <= self.rect.x + self.rect.width + 60 and piece.location[0] >= self.rect.x + 60:
                if piece.location[1] <= self.rect.y + self.rect.height + 60 and piece.location[1] >= self.rect.y + 60:
                    self.rect.x = location[0]
                    self.rect.y = location[1]
                    piece.rect.x = 700
                    piece.rect.y = 80
            elif piece.location[0] <= self.rect.x - self.rect.width - 60 and piece.location[0] >= self.rect.x +- 60:
                if piece.location[1] <= self.rect.y + self.rect.height + 60 and piece.location[1] >= self.rect.y + 60:
                    self.rect.x = location[0]
                    self.rect.y = location[1]
                    piece.rect.x = 700
                    piece.rect.y = 80
        '''
        pass

    def en_passe(self):
        '''
        if first:
            for piece in BlackPlayer.black_pieces:
                if piece.type == 'pawn':
                    if piece.location[0] <= self.rect.x + self.rect.width + 60 and piece.location[0] >= self.rect.x + 60:
                        if piece.location[1] <= self.rect.y + self.rect.height + 60 and piece.location[1] >= self.rect.y + 60:
                            self.rect.x = location[0]
                            self.rect.y = location[1]
                            piece.rect.x = 25
                            piece.rect.y = 80
                    elif piece.location[0] <= self.rect.x - self.rect.width - 60 and piece.location[0] >= self.rect.x +- 60:
                        if piece.location[1] <= self.rect.y + self.rect.height + 60 and piece.location[1] >= self.rect.y + 60:
                            self.rect.x = location[0]
                            self.rect.y = location[1]
                            piece.rect.x = 25
                            piece.rect.y = 80
            for piece in WhitePlayer.white_pieces:
                if piece.type == 'pawn':
                    if piece.location[0] <= self.rect.x + self.rect.width + 60 and piece.location[0] >= self.rect.x + 60:
                        if piece.location[1] <= self.rect.y + self.rect.height + 60 and piece.location[1] >= self.rect.y + 60:
                            self.rect.x = location[0]
                            self.rect.y = location[1]
                            piece.rect.x = 25
                            piece.rect.y = 80
                    elif piece.location[0] <= self.rect.x - self.rect.width - 60 and piece.location[0] >= self.rect.x +- 60:
                        if piece.location[1] <= self.rect.y + self.rect.height + 60 and piece.location[1] >= self.rect.y + 60:
                            self.rect.x = location[0]
                            self.rect.y = location[1]
                            piece.rect.x = 25
                            piece.rect.y = 80
        '''
        pass

    def promotion(self):
        if self.c == 'b':
            if self.rect.y >= 500 and self.rect.y <= 560:
                self.rect.x = 700
                self.rect.y = 45
        if self.c == 'w':
            if self.rect.y >= 40 and self.rect.y <= 100:
                self.rect.x = 25
                self.rect.y = 45

    def valid_move(self, x_pos, y_pos):
        if self.c == 'b':
            if self.first:
                if x_pos <= self.rect.x + self.rect.width + 60 and x_pos >= self.rect.x:
                    if y_pos <= self.rect.y + self.rect.height + 130 and y_pos >= self.rect.y:
                        return True
                else:
                    return False
            else:
                if x_pos <= self.rect.x + 60 and x_pos >= self.rect.x:
                    if y_pos <= self.rect.y + self.rect.height + 60 and y_pos >= self.rect.y:
                        return True
                else:
                    return False
        elif self.c == 'w':
            if self.first:
                if x_pos <= self.rect.x + self.rect.width + 60 and x_pos >= self.rect.x:
                    if y_pos >= self.rect.y - self.rect.height - 130 and y_pos <= self.rect.y:
                        return True
                else:
                    return False
            else:
                if x_pos <= self.rect.x + self.rect.width + 60 and x_pos >= self.rect.x:
                    if y_pos >= self.rect.y - self.rect.height - 60 and y_pos <= self.rect.y:
                        return True
                else:
                    return False

    def is_clicked(self, cor):
        if cor[0] >= self.rect.x and cor[0] <= self.rect.x + 23:
            if cor[1] >= self.rect.y and cor[1] <= self.rect.y + 52:
                self.click = True
                return True
        else:
            self.click = False
            return False
        
    def type(self):
        return 'pawn'
