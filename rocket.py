from turtle import Turtle

class Rocket(Turtle):
    
    def __init__(self, cor_x: int, cor_y: int):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.2)
        self.penup()
        self.goto(cor_x, cor_y)
        self.y_move = 7
        
    def move_up(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)
