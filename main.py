from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Scoreboard
from constants import *
import time


def game_over():
    ttl = Turtle()
    ttl.pencolor('white')
    ttl.penup()
    ttl.write('GAME OVER!', True, 'center', ('Arial', 30, 'bold'))


def hit_wall(snake):
    return int(abs(snake.head.xcor())) == int(BOARD_DIM/2) or \
        int(abs(snake.head.ycor())) == int(BOARD_DIM/2)


def hit_self(snake):
    segment_locs = [segment.pos() for segment in snake.segments]
    return snake.head.pos() in segment_locs[1:]


def main():
    # Initialize the game canvas
    canvas = Screen()
    canvas.setup(width=BOARD_DIM, height=BOARD_DIM)
    canvas.bgcolor('black')
    canvas.title("Snake Game")
    difficulty = canvas.numinput(prompt='Enter difficulty level (1 - 10): ',
                                 title='Difficulty level')
    canvas.tracer(0)

    # Initialize snake and food
    snake = Snake()
    food = Food()
    score = Scoreboard()

    # Move Snake
    is_on = True
    canvas.listen()
    while is_on:
        canvas.onkey(snake.left, 'Left')
        canvas.onkey(snake.right, 'Right')
        canvas.onkey(snake.up, 'Up')
        canvas.onkey(snake.down, 'Down')

        snake.move()
        if snake.head.distance(food) < 0.1:
            snake.extend()
            food.refresh()
            score.update()
        time.sleep(0.5 - 0.05 * (difficulty - 1))
        canvas.update()
        if hit_wall(snake) or hit_self(snake):
            is_on = False
            game_over()

    canvas.exitonclick()


if __name__ == '__main__':
    main()
