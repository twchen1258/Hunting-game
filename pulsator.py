# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    
    hungryCycle = 30
    
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.hungryCount = 0
        self.radius = Black_Hole.radius
        
    def update(self, model):
        eaten = Black_Hole.update(self,model)
        if len(eaten)!=0:
            self.hungryCount = 0
            for _ in eaten:
                self.change_dimension(1,1)
                self.radius += 0.5
        else:
            self.hungryCount+=1
            if self.hungryCount==Pulsator.hungryCycle:
                self.change_dimension(-1,-1)
                self.radius -= 0.5
                self.hungryCount = 0
                if self.get_dimension()==(0,0):
                    model.remove(self)  
                
        return eaten
    
