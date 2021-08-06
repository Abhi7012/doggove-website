import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("TURTLE_KING")
screen.setup(width=600, height=600)
screen.tracer(0)
cars=CarManager()
player=Player()
score=Scoreboard()
score.ht()
screen.listen()

screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    cars.Carmaker()
    cars.move()
    for i in cars.allcars:
        if player.distance(i)<50:
            score.st()
            score.lose()
            game_is_on=False
    if player.ycor()>260:
        score.st()
        score.Won()
        print("won")
        game_is_on=False
    time.sleep(0.1)
    screen.update()
    
    
    


screen.exitonclick()
