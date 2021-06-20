"""
OOP programming in python
"""
"""
import another_module
print(another_module.another_variable)

#import turtle
#timmy = turtle.Turtle()
#or
from turtle import Screen, Turtle
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

#timmy's screen
timmy_screen = Screen()
print(timmy_screen.canvheight)
timmy_screen.exitonclick()"""

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Car Name",["Ferrari","Tesla","Opel"])
table.add_column("Type",["Petrol","Electric","Gas"])

print(table)