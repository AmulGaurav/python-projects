import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(height=520)

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if guess == "Exit":
        states_missed = [state for state in all_states if state not in guessed_states]
        states_missed_dict = {"States to Learn" : states_missed}
        new_data = pandas.DataFrame(states_missed_dict)
        new_data.to_csv("states_to_learn.csv")
        break
    elif guess in all_states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = data[data.state == guess]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(guess)