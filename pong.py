from turtle import Turtle

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=0.50)


    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)

