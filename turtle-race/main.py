from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter your color: ")

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

all_turtles = []

y_positions = [90, 60, 30, 0, -30, -60, -90]

is_race_on = False

for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

            if turtle.xcor() > 230:
                is_race_on = False
                if user_bet == turtle.pencolor():
                    print(f"You've won! The {turtle.pencolor()} is the winnner.")
                else:
                    print(f"You've lost!, The {turtle.pencolor()} is the winner.")

screen.exitonclick()