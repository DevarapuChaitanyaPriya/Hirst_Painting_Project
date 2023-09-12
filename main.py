import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
colors = [(190, 160, 135), (236, 215, 192), (189, 145, 161), (239, 207, 220), (203, 230, 212), (142, 175, 156),
          (145, 165, 181), (206, 219, 233), (129, 98, 77), (210, 201, 153), (129, 84, 101), (226, 171, 187),
          (80, 117, 97), (86, 105, 121), (170, 104, 121), (230, 174, 164), (165, 208, 185), (174, 107, 96),
          (97, 147, 124), (144, 138, 94), (182, 184, 214), (64, 37, 20), (63, 27, 41), (160, 206, 213), (119, 120, 153),
          (93, 144, 152), (102, 44, 60), (25, 51, 35), (27, 41, 59), (79, 72, 35), (104, 45, 36), (42, 81, 54),
          (57, 57, 92), (32, 80, 85)]

potti = Turtle()

potti.setheading(225)
potti.penup()
potti.forward(250)
potti.pendown()
potti.setheading(0)
potti.speed("fastest")


def left_movement():
    potti.setheading(90)
    potti.forward(25)
    potti.setheading(180)
    potti.forward(25)


def right_movement():
    potti.setheading(90)
    potti.forward(25)
    potti.setheading(0)
    potti.forward(25)


def move_a_head():
    for value in range(20):
        potti.dot(10, random.choice(colors))
        potti.penup()
        potti.forward(25)


for i in range(10):
    move_a_head()
    left_movement()
    move_a_head()
    right_movement()

my_screen = Screen()
my_screen.exitonclick()
