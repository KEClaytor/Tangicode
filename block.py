# Basic block class
def cmp_block(a, b):
    print "(%d, %d) (%d, %d)" %(a.x, a.y, b.x, b.y)
    print "(%d, %d) (%d, %d)" %(a.w, a.h, b.w, b.h)
    if a.y > b.y+b.h:
        return 1
    elif (a.y > b.y) and (a.y < b.y+b.h):
        print "within bounds"
        if a.x > b.x:
            return 1
        elif a.x == b.x:
            return 0
        else:
            return -1
    else:
        return -1

class block():

    def __init__(self, position=(0,0), size=(0,0), mycolor=None, myaction=None):
        self.x, self.y = position
        self.w, self.h = size
        self.color = mycolor
        self.action = myaction
        
