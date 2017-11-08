#Andrew Parker
#10/1/17
#drawingProgram

from ggame import *

ROWS = 24 #original 24
COLS = 50 #original 50
CELL_SIZE = 20 #original 20


#moves painter right
def moveRight(event):
    if painter.x < (COLS-1)*CELL_SIZE:
        painter.x += CELL_SIZE
        if data["drawOnOff"] == True:
            startBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data["color"]),data["color"])
            Sprite(startBox,(painter.x,painter.y))
        
    
#moves painter left
def moveLeft(event):
    if painter.x > 0:
        painter.x -= CELL_SIZE
        if data["drawOnOff"] == True:
            startBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data["color"]),data["color"])
            Sprite(startBox,(painter.x,painter.y))
    
#moves painter up    
def moveUp(event):
    if painter.y > 0:
        painter.y -= CELL_SIZE
        if data["drawOnOff"] == True:
            startBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data["color"]),data["color"])
            Sprite(startBox,(painter.x,painter.y))
    
#moves painter down
def moveDown(event):
    if painter.y < (ROWS-1)*CELL_SIZE:
        painter.y += CELL_SIZE
        if data["drawOnOff"] == True:
            startBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data["color"]),data["color"])
            Sprite(startBox,(painter.x,painter.y))
                

#drawOff
def drawOnOff(event):
    if data["drawOnOff"] == False:
        data["drawOnOff"] = True
    else:
        data["drawOnOff"] = False


#changeColor
def changeColor(event):
    if event.key == "w":
        data["color"] = white
    elif event.key == "n":
        data["color"] = black
    elif event.key == "g":
        data["color"] = green
    elif event.key == "r":
        data["color"] = red
    elif event.key == "y":
        data["color"] = yellow
    elif event.key == "b":
        data["color"] = blue
    elif event.key == "o":
        data["color"] = orange
    elif event.key == "l":
        data["color"] = lightBlue
    elif event.key == "p":
        data["color"] = purple
    elif event.key == "u":
        data["color"] = brown
    
    


#runs the game
if __name__ == '__main__':
  
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    green = Color(0x00FF00,1) 
    red = Color(0xFF0000,1) 
    yellow = Color(0xFFFF00,1)
    blue = Color(0x0000FF,1) 
    
    orange = Color(0xFFA500,1)
    lightBlue = Color(0x00FFFF,1) 
    purple = Color(0x7F00FF,1) 
    darkPink = Color(0xFF007F,1)
    brown = Color(0x8B4513,1)
    
    data = {}
    data["drawOnOff"] = True
    data["color"] = black 

    
    BackBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,white),white)
    startBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,data["color"]),data["color"])


    Sprite(startBox,(300,100))
    painter = Sprite(startBox, (300,100))
 
    
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().listenKeyEvent('keydown','d',drawOnOff)
    
    App().listenKeyEvent('keydown','w',changeColor)
    App().listenKeyEvent('keydown','n',changeColor)
    App().listenKeyEvent('keydown','g',changeColor)
    App().listenKeyEvent('keydown','r',changeColor)
    App().listenKeyEvent('keydown','b',changeColor)
    App().listenKeyEvent('keydown','y',changeColor)
    
    App().listenKeyEvent('keydown','o',changeColor)
    App().listenKeyEvent('keydown','l',changeColor)
    App().listenKeyEvent('keydown','p',changeColor)
    App().listenKeyEvent('keydown','u',changeColor)
    
    
    App().run()