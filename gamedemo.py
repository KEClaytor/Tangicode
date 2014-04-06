# A simple sandbox game to demo the movement

import pygame, sys
from pygame.locals import *
import time

greenColor = pygame.Color(0, 255, 0)
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)

class player:

    def __init__(self, cx, pxh, ngrid):
        self.x, self.y = cx
        self.h = pxh
        self.ngrid = ngrid
        self.screen = pygame.Surface((pxh, pxh))
        self.screen.set_colorkey(greenColor)
        playerimg = pygame.image.load("krogan.jpg").convert()
        self.screen.blit(playerimg, (0, 0))

    def getsurface(self):
        return self.screen

    def getblitcoords(self):
        return (self.x*self.h, self.y*self.h)

    def moveleft(self):
        self.x -= 1
        if self.x < 0:
            self.x = 0

    def moveright(self):
        self.x += 1
        if self.x > self.ngrid:
            self.x = self.ngrid-1

    def moveup(self):
        self.y -= 1
        if self.y < 0:
            self.y = 0

    def movedown(self):
        self.y += 1
        if self.y > self.ngrid:
            self.y = self.ngrid-1

def drawgrid(res, pxh, grid):
    screen = pygame.Surface(res)
    nx = len(grid)
    ny = len(grid[0])
    offset = pxh/10
    mysize = 80*pxh/100
    for x in range(nx):
        for y in range(ny):
            ini = ((x)*pxh+offset, (y)*pxh+offset)
            wh = (mysize, mysize)
            pygame.draw.rect(screen, greenColor, pygame.Rect(ini, wh))
    return screen

def drawcapture(res):
    screen = pygame.Surface(res)
    capture = pygame.image.load("test.jpg").convert()
    screen.blit(capture, (0, 0))
    return screen

def run(blocks):
    pygame.init()
    fpsClock = pygame.time.Clock()

    screen_size = (1300,700)
    window = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Tangicode')

    sw = window.get_width()
    sh = window.get_height()

    # Display our custom grid
    # TODO: Import a grid
    ngrid = 5
    grid = [[0]*ngrid]*ngrid
    gridsize = sh/ngrid
    background = drawgrid((sw, sh), gridsize, grid)
    capturesurface = drawcapture((sw-sh, sh))
    # Add the player
    myplayer = player((2,3), gridsize, ngrid)
    # Execute the moves
    blockidx = 0
    while True:
        window.fill(blackColor)
        # Show the grid
        window.blit(background, (0,0))
        # Show the player
        window.blit(myplayer.getsurface(), myplayer.getblitcoords())
        # Draw the captured image
        window.blit(capturesurface, (sh, 0))
        # Get user key presses
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            else:
                if blockidx > len(blocks):
                    pygame.quit()
                    sys.exit()
                else:
                    block = blocks[blockidx]
                    if block.action == "left":
                        myplayer.moveleft()
                    elif block.action == "right":
                        myplayer.moveright()
                    elif block.action == "up":
                        myplayer.moveup()
                    elif block.action == "down":
                        myplayer.movedown()
                    time.sleep(1)

        #pygame.display.update()
        pygame.display.flip()
        fpsClock.tick(30)

    return True

if __name__ == "__main__":
    pygame.init()
    fpsClock = pygame.time.Clock()

    screen_size = (1300,700)
    window = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Tangicode')

    sw = window.get_width()
    sh = window.get_height()

    # Display our custom grid
    # TODO: Import a grid
    ngrid = 5
    grid = [[0]*ngrid]*ngrid
    gridsize = sh/ngrid
    background = drawgrid((sw, sh), gridsize, grid)
    capturesurface = drawcapture((sw-sh, sh))
    # Add the player
    myplayer = player((2,3), gridsize, ngrid)
    # Execute the moves
    while True:
        window.fill(blackColor)
        # Show the grid
        window.blit(background, (0,0))
        # Show the player
        window.blit(myplayer.getsurface(), myplayer.getblitcoords())
        # Draw the captured image
        window.blit(capturesurface, (sh, 0))
        # Get user key presses
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    myplayer.moveleft()
                elif event.key == K_RIGHT:
                    myplayer.moveright()
                elif event.key == K_UP:
                    myplayer.moveup()
                elif event.key == K_DOWN:
                    myplayer.movedown()

        #pygame.display.update()
        pygame.display.flip()
        fpsClock.tick(30)

