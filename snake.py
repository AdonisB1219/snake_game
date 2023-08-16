from turtle import Turtle, Screen
import time
import random


class Snake:

    def __init__(self, color):
        self.c = color
        self.create_snake()

    def create_snake(self):
        self.snake_body = []
        self.head = Turtle("square")
        self.head.color(self.c)
        self.head.penup()
        self.snake_body.append(self.head)
        self.add_segment()
        self.add_segment()

    def add_segment(self):
        new_seg = Turtle("square")
        new_seg.color(self.c)
        new_seg.penup()
        new_position = self.snake_body[-1].pos()
        new_seg.setpos(new_position)
        self.snake_body.append(new_seg)

    def move(self):
        for seg in range(len(self.snake_body) - 1, 0,-1):
            new_pos = self.snake_body[seg - 1].pos()
            self.snake_body[seg].setpos(new_pos)
        self.snake_body[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


