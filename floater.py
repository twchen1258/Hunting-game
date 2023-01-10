# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import uniform, randint


class Floater(Prey): 
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,2*Floater.radius,2*Floater.radius,0,5)
        self.randomize_angle()
    
    def update(self, model):
        if randint(1,100)<=30:
            newSpeed = self.get_speed() + uniform(-0.5,0.5)
            if newSpeed>=7.0:
                newSpeed = 7.0
            elif newSpeed <= 3.0:
                newSpeed = 3.0
                
            newAngle = self.get_angle() + uniform(-0.5,0.5)
            self.set_velocity(newSpeed, newAngle)
            
        self.move()
    
    def display(self, canvas):
        x, y = self.get_location()
        canvas.create_oval(x-Floater.radius, y-Floater.radius,
                            x+Floater.radius, y+Floater.radius,
                                fill="red")
