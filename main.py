import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('My Snake Game')
screen.tracer(0)  # off tracing turtle on screen

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkeypress(key='Left', fun=snake.left)
screen.onkeypress(key='Right', fun=snake.right)
screen.onkeypress(key='Up', fun=snake.up)
screen.onkeypress(key='Down', fun=snake.down)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh_food()
        score.update_score()
        snake.extend()

    # Detect collision with wall
    if snake.snake_head.xcor() >= 298 or snake.snake_head.ycor() >= 298 or snake.snake_head.xcor() <= -298 or snake.snake_head.ycor() <= -298:
        # score.game_over()
        # game_is_on = False
        score.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            # score.game_over()
            # game_is_on = False
            score.reset()
            snake.reset_snake()


screen.exitonclick()
