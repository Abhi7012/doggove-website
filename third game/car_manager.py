import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.allcars=[]
        
        self.Carmaker()

        

        
    def Carmaker(self):
        chance=random.randint(1,10)
        if chance==1:
            x=Turtle("square")
            x.shapesize(1,2)
            x.rt(180)
            x.color(random.choice(COLORS))
            x.penup()
            x.goto(300,random.randint(-240,240))
            self.allcars.append(x)
       
    def move(self):
        for i in self.allcars:
            i.fd(STARTING_MOVE_DISTANCE)

     




        
