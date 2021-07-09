import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.penup()
        self.speed('fastest')
        self.refresh_food()

    def refresh_food(self):
        self.setposition(random.randint(-280, 280), random.randint(-280, 280))
