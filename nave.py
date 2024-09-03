from turtle import Turtle
from rocket import Rocket

class Nave(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("triangle")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.left(90)
        self.penup()
        self.goto(0,-200)
        self.rocket = None
        
    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > -360:
            self.goto(new_x, self.ycor())
    
    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < 360:
            self.goto(new_x, self.ycor())

    def shoot_rocket(self):
        if not self.rocket:
            self.rocket = Rocket(self.xcor(), self.ycor() + 10)
    
    def remove_rocket(self):
        self.rocket.clear()
        self.rocket.hideturtle()
        self.rocket = None
    
    def reset_position(self):
        self.goto(0,-200)