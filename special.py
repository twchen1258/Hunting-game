# A Special class is similar to a hunter. It is derived from a Pulsator and then Mobile_Simulton base.
# It exhibits the behavior of a hunter object, with two differences. First, it changes color every 0.1 second.
# Secondly, when it detects a prey in its view range, it with speed up to 7 pixels/update. On the other hand, when 
# there is no prey in its range, it will moves at 5 pixels/update. Because this ability is too powerful, the Special 
# object have only 100 pixel view range.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import random

class Special(Pulsator, Mobile_Simulton):  
    
    viewRange = 100
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,2*self.radius,2*self.radius,0,5)
        self.randomize_angle()
        
    def update(self, model):
        Pulsator.update(self,model)
        target = set()
        for b in model.find(lambda x: isinstance(x, Prey)):
            if self.distance(b.get_location())<=Special.viewRange:
                target.add(b)
        if len(target)==0:
            self.set_speed(5)
            self.move()
        else:
            rabbit = target.pop()
            distance = self.distance(rabbit.get_location())
            for i in target:
                if self.distance(i.get_location())<distance:
                    rabbit = i
                    distance = self.distance(i.get_location())
            px,py = rabbit.get_location()
            hx,hy = self.get_location()
            self.set_velocity(7, atan2(py-hy, px-hx))
            
            self.move()
            
    def display(self, canvas):
        x,y = self.get_location()
        canvas.create_oval(x-self.radius, y-self.radius,
                            x+self.radius, y+self.radius,
                            fill="#"+''.join([random.choice('ABCDEF0123456789') for _ in range(6)]))