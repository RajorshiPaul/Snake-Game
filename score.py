from turtle import Turtle
from constants import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, BOARD_DIM/2 - 30)
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.write(f'Score: {self.score}', True, 'center',
                   ('Arial', 20, 'bold'))

    def update(self):
        self.clear()
        self.score += 1
        self.goto(0, BOARD_DIM / 2 - 30)
        self.write(f'Score: {self.score}', True, 'center',
                   ('Arial', 20, 'bold'))
