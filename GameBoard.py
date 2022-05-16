import pygame
from pygame.locals import *
import os
from Knight import *
from King import *
from Queen import *
from Rook import *
from Pawn import *
from Bishop import *
from BlackPlayer import *
from WhitePlayer import *


#screen setup
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.key.set_repeat(100,100)

#loads board game picture
board = pygame.image.load(os.path.join('Images', 'game board.png'))

#loads the black player and its pieces
black_player = BlackPlayer()
black_player.add(Bishop(490, 50, 'b'))
black_player.add(Bishop(300, 50, 'b'))
black_player.add(Knight(235, 50, 'b'))
black_player.add(Knight(555, 50, 'b'))
black_player.add(Rook(615, 50, 'b'))
black_player.add(Rook(169, 50, 'b'))
black_player.add(Pawn(170, 120, 'b'))
black_player.add(Pawn(235, 120, 'b'))
black_player.add(Pawn(298, 120, 'b'))
black_player.add(Pawn(362, 120, 'b'))
black_player.add(Pawn(425, 120, 'b'))
black_player.add(Pawn(490, 120, 'b'))
black_player.add(Pawn(553, 120, 'b'))
black_player.add(Pawn(618, 120, 'b'))
black_player.add(King(425, 43, 'b'))
black_player.add(Queen(362, 45, 'b'))

#loads the white player and its pieces
white_player = WhitePlayer()
white_player.add(Bishop(490, 510, 'w'))
white_player.add(Bishop(300, 510, 'w'))
white_player.add(Knight(235, 510, 'w'))
white_player.add(Knight(555, 510, 'w'))
white_player.add(Rook(615, 510, 'w'))
white_player.add(Rook(169, 510, 'w'))
white_player.add(Pawn(170, 450, 'w'))
white_player.add(Pawn(235, 450, 'w'))
white_player.add(Pawn(298, 450, 'w'))
white_player.add(Pawn(362, 450, 'w'))
white_player.add(Pawn(425, 450, 'w'))
white_player.add(Pawn(490, 450, 'w'))
white_player.add(Pawn(553, 450, 'w'))
white_player.add(Pawn(618, 450, 'w'))
white_player.add(King(425, 503, 'w'))
white_player.add(Queen(362, 506, 'w'))

click = 0
temp = (0, 0)
play = ""
offset_x = 0
offset_y = 0
end = True
while end:
    #fills the screen and places board and piece images on screen
    screen.fill((99, 50, 1))
    screen.blit(board, (150, 40))
    clock.tick(100)
    black_player.draw(screen)
    white_player.draw(screen)

    for event in pygame.event.get():
        #exits screen if user presses escape or quits the screen
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click += 1

    if click < 2:
        temp = pygame.mouse.get_pos()
        for player in black_player.black_pieces:
            if player.is_clicked(temp):
                play = player
        if play == "":
            for p in white_player.white_pieces:
                if p.is_clicked(temp):
                    play = p
    elif click == 2:
        click = 0
        offset_x = play.rect.width/2
        offest_y = play.rect.height/2
        pos = pygame.mouse.get_pos()
        play.move(pos[0] - offset_x, pos[1] - offset_y)

    pygame.display.update()
