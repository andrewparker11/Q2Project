#Andrew Parker
#
#drawingProgram

from ggame import *

ROWS = 24
COLS = 50
CELL_SIZE = 20


#moves painter right
def moveRight(event):
    if painter.x < (COLS-1)*CELL_SIZE:
        painter.x += CELL_SIZE
        Sprite(startBox,(painter.x,painter.y))
    
#moves painter left
def moveLeft(event):
    if painter.x > 0:
        painter.x -= CELL_SIZE
        Sprite(startBox,(painter.x,painter.y))
    
#moves painter up    
def moveUp(event):
    if painter.y > 0:
        painter.y -= CELL_SIZE
        Sprite(startBox,(painter.x,painter.y))
    
#moves painter down
def moveDown(event):
    if painter.y < (ROWS-1)*CELL_SIZE:
        painter.y += CELL_SIZE
        Sprite(startBox,(painter.x,painter.y))


#drawOff
def drawOnOff(event):
    if data["drawOnOff"] == False:
        data["drawOnOff"] == True
    else:
        data["drawOnOff"] == False

"""  
#changeColorGreen
def greenColor(event):
    if data"""


#runs the game
if __name__ == '__main__':
    
    data = {}
    data["drawOnOff"] = True
    
    
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
 
    
    BackBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,white),white)
    startBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),black)

    
    Sprite(startBox,(300,100))
    painter = Sprite(startBox, (300,100))
 
    """
    data["greenColor"] = False
    data["redColor"] = False
    data["blueColor"] = False
    data["yellowColor"] = False
    App().listenKeyEvent('keydown','g',greenColor)
    App().listenKeyEvent('keydown','r',redColor)
    App().listenKeyEvent('keydown','b',blueColor)
    App().listenKeyEvent('keydown','y',yellowColor)
    """
    
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().listenKeyEvent('keydown','d',drawOnOff)
    App().run()