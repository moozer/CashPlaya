class point(object):
    ''' point class: basic x,y with add and subtract '''
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def __add__(self, otherpoint ):
        assert(  issubclass( type(otherpoint), point) )
        return point( self.x+otherpoint.x, self.y+otherpoint.y)
    
    def __sub__(self, otherpoint ):
        return point( self.x-otherpoint.x, self.y-otherpoint.y)
    
    def __eq__(self, otherpoint):
        return (self.x == otherpoint.x) & (self.y == otherpoint.y)

    def __mul__(self, multiplier):
        return point( multiplier*self.x, multiplier* self.y )

    __rmul__ = __mul__
    
    @property
    def tupple(self):
        return self.x, self.y
    
    def __str__(self):
        return "point: (%d, %d)"%(self.x, self.y)