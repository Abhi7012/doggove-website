from turtle import Turtle, circle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        x=random.randint(-880,880)
        y=random.randint(-580,580)
        self.goto(x,y)
