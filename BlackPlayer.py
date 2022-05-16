from Knight import *
from King import *
from Queen import *
from Rook import *
from Pawn import *
from Bishop import *

class BlackPlayer():
    def __init__ (self):
        self.black_pieces = pygame.sprite.Group()

    def add(self, piece):
        self.black_pieces.add(piece)

    def draw(self, win):
        for p in self.black_pieces:
            p.draw(win)

    def show(self):
        return self.black_pieces
