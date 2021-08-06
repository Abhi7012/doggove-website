from turtle import Turtle
import turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(3,3)
        self.color("black")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)
    def move(self):
        self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)
