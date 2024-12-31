from turtle import Turtle

START_POSITIONS = [(0,0), (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for position in START_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_snake = Turtle()
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        for segment in range(len(self.segments)-1, 0, -1):
            xcor = self.segments[segment-1].xcor()
            ycor = self.segments[segment-1].ycor()
            self.segments[segment].goto(xcor,ycor)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)