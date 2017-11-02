#Andrew Parker
#
#drawingProgram

from ggame import *

ROWS = 24
COLS = 50
CELL_SIZE = 20


#moves monkey right
def moveRight(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
    
    
#moves monkey left
def moveLeft(event):
    if monkey.x > 0:
        monkey.x -= CELL_SIZE
    
    
#moves monkey up    
def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE

    
#moves monkey down
def moveDown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE:
        monkey.y += CELL_SIZE
        

    
#runs the game
if __name__ == '__main__':
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    red = Color(0xFF0000,1) 
    yellow = Color(0xFFFF00,1)
    orange = Color(0xFFA500,1)
    green = Color(0x00FF00,1) 
    lightBlue = Color(0x00FFFF,1) 
    blue = Color(0x0000FF,1) 
    purple = Color(0x7F00FF,1) 
    darkPink = Color(0xFF007F,1)
    brown = Color(0x8B4513,1)
 
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,white),white)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)

    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    
    
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)