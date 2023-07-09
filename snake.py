from turtle import Turtle
from constants import *


class Snake(Turtle):

    def __init__(self):
        self.segments = []
        self.initialize()
        self.head = self.segments[0]

    def initialize(self):
        for i in range(3):
            self.add_segment((-20*i, 0))

    def add_segment(self, position):
        ttl = Turtle()
        ttl.fillcolor('green')
        ttl.shape('square')
        ttl.penup()
        ttl.goto(position)
        self.segments.append(ttl)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.segments[0].forward(STEP_SIZE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
