from turtle import Screen
import time
import random
from snake import Snake
from scoreboard import Scoreboard
from food import Food

game_on = True
scoreboard = Scoreboard()
score = 0


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.listen()
snake_color = screen.textinput("color", "What color do you want your snake?").lower()

snake = Snake(snake_color)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
food = Food()
screen.tracer(0)

while game_on:
    scoreboard.update_score(score)
    snake.move()
    screen.update()
    time.sleep(0.1)

    if food.distance(snake.head) < 15:
        food.update_food()
        snake.add_segment()
        score += 1
        scoreboard.update_score(score)

    for seg in snake.snake_body[1:]:
        if seg.distance(snake.head) < 10:
            scoreboard.game_over()
            game_on = False

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()