import turtle

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    tim.right(5)

def turn_left():
    tim.left(5)

def clear_screen():
    screen.reset()
    tim.width(3)

tim = turtle.Turtle()
tim.width(3)                #increases pen width of turtle

screen = turtle.Screen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.listen()

screen.exitonclick()