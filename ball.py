from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self, cord_x: int, cord_y: int):
        super().__init__()
        self.color("green")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.2)
        self.penup()
        self.goto(cord_x, cord_y)
        self.y_move = 7
        
    def move_down(self):
        new_y = self.ycor() - self.y_move
        self.goto(self.xcor(), new_y)
        
    def remove_ball(self):
        self.clear()
        self.hideturtle()