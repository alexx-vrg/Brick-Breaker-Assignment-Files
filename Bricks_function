#Creating the bricks function

import turtle
import random


def create_bricks():
    #Adjust the domain and horizontal step
    for x in range(-765, 785, 85):
        #Adjust the range and vertical step
        for y in range(200, 450, 25):
            brick = turtle.Turtle()
            brick.shape("square")
            #List of different colors for each brick
            colors = ["red", "yellow", "green", "purple"]
            #Make the colors random for every brick
            brick_color = random.choice(colors)
            colors.remove(brick_color)
            brick.color(brick_color)
            #Define the bricks sizes
            brick.shapesize(stretch_wid=1, stretch_len=4)
            brick.penup()
            brick.goto(x, y)
