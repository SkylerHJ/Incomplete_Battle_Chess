from Knight import *
from King import *
from Queen import *
from Rook import *
from Pawn import *
from Bishop import *

class WhitePlayer():
    def __init__ (self):
        self.white_pieces = pygame.sprite.Group()

    def add(self, piece):
        self.white_pieces.add(piece)

    def draw(self, win):
        for p in self.white_pieces:
            p.draw(win)
