from turtle import *
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","purple","green","yellow","orange","blue"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []

#set the starting positions
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won the race: winner: {user_bet}")
            else:
                print(f"You've lost! winner: {winning_color}")
            is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()