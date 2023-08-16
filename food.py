from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.goto(randint(-250, 250), randint(-250, 250))

    def update_food(self):
        self.goto(randint(-250, 250), randint(-250, 250))


