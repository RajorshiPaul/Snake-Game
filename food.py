from turtle import Turtle
from random import choice
from constants import *

LIMIT = int(BOARD_DIM / 2) - 20

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.shape('circle')
        self.fillcolor('red')
        self.refresh()

    def refresh(self):
        array = range(-LIMIT, LIMIT, 20)
        self.setx(choice(array))
        self.sety(choice(array))
