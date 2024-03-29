import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SHAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
start_position = [(0, 0), (-20, 0), (-40, 0)]
screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 25:
        food.refresh()
        score.increase_score()
        snake.extand()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reser()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.reset()
            snake.reser()

screen.exitonclick()