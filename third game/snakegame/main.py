from turtle import Screen, Turtle
import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1900, height=1200)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    

    snake.move()
    if snake.head.distance(food)<20:
        snake.extend_segment()
        food.refresh()
        scoreboard.score()
    if snake.head.xcor()>940 or snake.head.xcor()<-940 or snake.head.ycor()>580 or snake.head.ycor()<-580:
        scoreboard.reset()
        snake.reset()
        
    if snake.detection_with_tail():
        scoreboard.reset()
        snake.reset()
    
print("GAME ENDED")


screen.exitonclick()