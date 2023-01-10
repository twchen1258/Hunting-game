# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    
    viewRange = 200
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,2*self.radius,2*self.radius,0,5)
        self.randomize_angle()
        
    def update(self, model):
        Pulsator.update(self,model)
        target = set()
        for b in model.find(lambda x: isinstance(x, Prey)):
            if self.distance(b.get_location())<=Hunter.viewRange:
                target.add(b)
        if len(target)==0:
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
            self.set_angle(atan2(py-hy, px-hx))
            
            self.move()
            
        
        