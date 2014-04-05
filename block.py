# Basic block class

class block():

    def __init__(self, position=(0,0), mycolor=None, myaction=None):
        self.x,self.y = position
        self.color = mycolor
        self.action = myaction
        
