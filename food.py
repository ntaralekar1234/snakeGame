from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed("fastest")
        xcor = random.randint(-280,280)
        ycor = random.randint(-280, 280)
        self.goto(xcor,ycor)

    def refresh(self):
        xcor = random.randint(-280, 280)
        ycor = random.randint(-280, 280)
        self.goto(xcor, ycor)