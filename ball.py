# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey


class Ball(Prey): 
    
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,2*Ball.radius,2*Ball.radius,0,5)
        self.randomize_angle()
    
    def update(self, model):
        self.move()
    
    def display(self, canvas):
        x, y = self.get_location()
        canvas.create_oval(x-Ball.radius, y-Ball.radius,
                            x+Ball.radius, y+Ball.radius,
                                fill="blue")
    
