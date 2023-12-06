import turtle
from turtle import Turtle
import math
import random

class Ball(Turtle):
    def __init__(self, paddle):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(10, -150)
        self.move_dist_x = 0
        self.move_dist_y = -10
        self.move_speed = 0.05
        self.paddle = paddle  # Store the paddle instance

    def movement(self):
        new_x = self.xcor() + self.move_dist_x
        new_y = self.ycor() + self.move_dist_y
        self.goto(new_x, new_y)

        # Check for collisions with walls
        if new_x > 800 or new_x < -800:
            self.bounce_x()

        if new_y > 450 or new_y < -450:
            self.bounce_y()

        # Check for collisions with the paddle
        if (
            new_y < -250
            and self.paddle.xcor() - 50 < new_x < self.paddle.xcor() + 50
        ):
            self.bounce_y()

    def bounce_x(self):
        self.move_dist_x *= -1

    def bounce_y(self):
        # Calculate the current angle of movement
        current_angle = math.degrees(math.atan2(self.move_dist_y, self.move_dist_x))

        # Check if the ball is hitting the left or right wall
        if self.xcor() > 0:  # Ball is on the right side of the screen
            bounce_angle_degrees = 240
        else:  # Ball is on the left side of the screen
            bounce_angle_degrees = 300

        # If the ball is hitting a wall, set the bounce angle to 180 degrees
        if abs(self.ycor()) > 450:
            bounce_angle_degrees = 180

        # Calculate the new angle after bouncing
        new_angle = 2 * bounce_angle_degrees - current_angle

        # Convert the angle back to radians
        new_angle_radians = math.radians(new_angle)

        # Calculate the new x and y components based on the new angle
        magnitude = math.sqrt(self.move_dist_x**2 + self.move_dist_y**2)
        self.move_dist_x = magnitude * math.cos(new_angle_radians)
        self.move_dist_y = magnitude * math.sin(new_angle_radians)

    def start(self):
        self.move_dist_y = -10  # Start moving downward
