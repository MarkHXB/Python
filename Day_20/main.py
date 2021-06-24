from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#setup the gameboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#snake's segments or snake body
segments = []


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

#input
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#main loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 290  or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10 :
            game_is_on = False
            scoreboard.game_over()


#exit events
screen.exitonclick()
