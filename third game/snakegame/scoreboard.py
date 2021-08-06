from turtle import Turtle
with open("/Users/me/Desktop/New folder/third game/snakegame/data.txt") as hs:
    highscore=hs.readline()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.goto(0,500)
        self.Score=0
        self.highscore=int(highscore)
        self.ht()
        self.updatescore()
    
    def updatescore(self):
        self.clear()
        self.write(f"SCORE : {self.Score} HIGHSCORE : {self.highscore}",align="center",font=("Courier", 24, "normal"))
        
        

    def score(self):
        self.Score+=50
        self.updatescore()
    
    def reset(self):
        if self.Score>self.highscore:
            self.highscore=self.Score
            with open("/Users/me/Desktop/New folder/third game/snakegame/data.txt","w") as whs:
                whs.write(str(self.highscore))
            
        self.Score=0
        self.updatescore()
    

         