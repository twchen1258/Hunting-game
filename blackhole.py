# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,2*Black_Hole.radius,2*Black_Hole.radius)
    
    def update(self, model):
        s = set()
        for b in model.find(lambda x: isinstance(x, Prey)):
            if self.contains(b.get_location()):
                s.add(b)
                model.remove(b)
        return s
    
    def display(self, canvas):
        x, y = self.get_location()
        canvas.create_oval(x-self.radius, y-self.radius,
                            x+self.radius, y+self.radius,
                                fill="black")
    
    def contains(self, xy):
        return self.distance(xy) <= self.radius
