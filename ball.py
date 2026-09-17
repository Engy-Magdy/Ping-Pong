from turtle import Turtle,Screen
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("normal")
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
    
