from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_in in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=turtle_in * 25)
    new_turtle.color(colors[turtle_in])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"you win {turtle.pencolor()}")
            else:
                print(f"you lose{turtle.pencolor()}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)






screen.exitonclick()

tom = Turtle(shape="turtle")
# tom.penup()
# tom.goto(x=-230, y=-100)
#
#
# tam = Turtle(shape="turtle")
# tam.penup()
# tam.goto(x=-230, y=-50)
#
#
# tem = Turtle(shape="turtle")
# tem.penup()
# tem.goto(x=-230, y=0)
#
#
# tym = Turtle(shape="turtle")
# tym.penup()
# tym.goto(x=-230, y=50)