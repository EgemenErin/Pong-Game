from turtle import Turtle, Screen
from pong import Pong
from random import randint
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

pong = Pong()
pong.goto(-280, 0)
pong2 = Pong()
pong2.goto(270, 0)
screen.listen()
screen.onkey(pong.up, "Up")
screen.onkey(pong.down, "Down")
screen.onkey(pong2.up, "W")
screen.onkey(pong2.down, "S")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
screen.exitonclick()