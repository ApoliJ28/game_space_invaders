from turtle import Turtle
from ball import Ball
import random

COLOR = "green"
X = 180

class Aliens:
    
    def __init__(self):
        self.all_alien = []
        self.firts_aliens = []
        self.last_aliens = []
        self.shoot_balls = []
        self.create_all_aliens()
        self.x_move = 4
    
    def create_all_aliens(self):
        y = 200
        
        for _ in range(1, 5):
            x = -X
            while x < X:
                if x == -X:
                    new_alien = Turtle("turtle")
                    new_alien.shapesize(stretch_len=1, stretch_wid=1)
                    new_alien.hideturtle()
                    new_alien.right(90)
                    new_alien.goto(x, y)
                    self.firts_aliens.append(new_alien)
                elif x >= X-30:
                    new_alien = Turtle("turtle")
                    new_alien.shapesize(stretch_len=1, stretch_wid=1)
                    new_alien.hideturtle()
                    new_alien.right(90)
                    new_alien.goto(x, y)
                    self.last_aliens.append(new_alien)
                new_alien = Turtle("turtle")
                new_alien.shapesize(stretch_len=1, stretch_wid=1)
                new_alien.penup()
                new_alien.color(COLOR)
                new_alien.right(90)
                new_alien.goto(x, y)
                self.all_alien.append(new_alien)
                x+=30
            y -= 30
            
    def move(self):
        for alien in self.all_alien:
            new_x = alien.xcor() + self.x_move
            alien.goto(new_x, alien.ycor())
        
        for firt_alien in self.firts_aliens:
            new_x = firt_alien.xcor() + self.x_move
            firt_alien.goto(new_x, firt_alien.ycor())
    
        for last_alien in self.last_aliens:
            new_x = last_alien.xcor() + self.x_move
            last_alien.goto(new_x, last_alien.ycor())
        
    def bounce_x_aliens(self):
        self.x_move *= -1
    
    def shoot_alien(self):
        alien = random.choice(self.all_alien)
        
        self.shoot_balls.append(Ball(alien.xcor(), alien.ycor()))
    
    def remove_all_balls(self):
        for ball in self.shoot_balls:
            ball.clear()
            ball.hideturtle()
            self.shoot_balls.remove(ball)
