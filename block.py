# Basic block class

class block():
    x,y = None
    mycolor = None
    myaction = None

    def __init__(self, position=(0,0), color=None, action=None):
        x,y = position
        mycolor = color
        myaction = action
        
