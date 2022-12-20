import turtle as t
import colorgram
import random

def rgb_color_list():
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

t.colormode(255)

colors = colorgram.extract('hirst-painting/image.jpg', 30)

rgb_colors = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

tim = t.Turtle()

tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
x_coordinate = tim.xcor()

for i in range(10):
    for j in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(50)
    tim.goto(x_coordinate, tim.ycor() + 50)