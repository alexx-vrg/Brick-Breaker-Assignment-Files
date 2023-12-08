import time
from turtle import Turtle
import random


#define the interface colors of the game 
FONT = ("Helvetica", 50, "normal")
ALIGNMENT = 'center'
COLOR = "white"
COLOR_LIST = ['light blue', 'royal blue', 'light steel blue',
			'light cyan', 'light sky blue', 'violet',
			'salmon', 'tomato','sandy brown',
			'purple', 'deep pink', 'medium sea green', 'khaki']

#put the interface in a class to make it easier to call variables
class Interface(Turtle):

	#draw the interface and choose a random color for the title "Brick breaker"
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.color(random.choice(COLOR_LIST))
		self.header()


	#make the header for the game
	def header(self):
		self.clear()
		self.goto(x=0, y=-185)
		self.write('Brick Breaker', align=ALIGNMENT, font=FONT)
		self.goto(x=0, y=-180)

	#choose a random color for every new life
	def change_color(self):
		self.clear()
		self.color(random.choice(COLOR_LIST))
		self.header()


	#define when the game is over
	def game_over(self, win):
		self.clear()
		if win == True:
			self.write('You won!', align=ALIGNMENT, font=FONT)
		else:
			self.write("Game Over", align=ALIGNMENT, font=FONT)
