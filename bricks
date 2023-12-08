from turtle import Turtle
import random

COLOR_LIST = ['light blue', 'royal blue', 
			'light steel blue', 'steel blue',
			'light cyan', 'light sky blue', 
			'violet', 'salmon', 'tomato', 'yellow', 'light green',
			'purple', 'deep pink', 'indian red', 'medium sea green',] #this is a list of all the colours already in python

weights = [1, 1, 1, 1, 1, 1, 1, 1, 1,
		   2, 2, 2, 2, 2, 2,
		   3, 3, 3, 3, 3] #the probability that a brick breaks when it is hit

class Brick(Turtle):
	def __init__(self, x_cor, y_cor): 
		super().__init__()
		self.penup()  #we give the individual brick characteristics, applied to all the bricks:
		self.shape('square') 
		self.shapesize(stretch_wid=1.5, stretch_len=3)
		self.color(random.choice(COLOR_LIST)) #from random, we choose a random colour for the brick to be
		self.goto(x=x_cor, y=y_cor) #set coordinates for the bricks

		self.quantity = random.choice(weights)

		# Defining borders of the brick
		self.left_wall = self.xcor() - 30 #the borders of the brick defined in terms of its coordinates
		self.right_wall = self.xcor() + 30
		self.upper_wall = self.ycor() + 15
		self.bottom_wall = self.ycor() - 15

#we create all the bricks:
class Bricks:
	def __init__(self): 
		self.y_start = 0 this initializes the x and y coordinates
		self.y_end = 210
		self.bricks = []
		self.create_all_lanes()

	def create_lane(self, y_cor): 
		for i in range(-570, 570, 63): #this gives each brick (for i is a brick) its coordinates
			brick = Brick(i, y_cor)
			self.bricks.append(brick)

	def create_all_lanes(self): 
		for i in range(self.y_start, self.y_end, 32): 
			self.create_lane(i) #we create the rows of bricks
