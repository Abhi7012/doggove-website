from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        

    def Won(self):
        self.color("green")
        self.write("YOU\nWON",align="center",font=FONT)

    def lose(self):
        self.color("green")
        self.write("YOU\nLOSE",align="center",font=FONT)

    
