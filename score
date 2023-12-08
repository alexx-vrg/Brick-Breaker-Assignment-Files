#the code below is responsble for handling the score of the brick breaker game
from turtle import Turtle
#if a file does not exist, it creates a new file and initiates it to zero
try:
	score = int(open('highestScore.txt', 'r').read())
except FileNotFoundError:
	score = open('highestScore.txt', 'w').write(str(0))
#if the file contains an invalid value, it resets to zero
except ValueError:
	score = 0
FONT = ('arial', 20, 'normal')


class Score(Turtle):
	def __init__(self, lives):
		super().__init__()
		self.color('white')
		self.penup()
		self.hideturtle()
		self.highScore = score
		self.goto(x=-580, y=260)
		self.lives = lives
		self.score = 0
		self.update_score()

	def update_score(self):
		self.clear()
		self.write(f"Score: {self.score} | Highest Score: \
		{self.highScore} | Lives: {self.lives}", align='left', 
				font=FONT)

	def increase_score(self):
		self.score += 1
		if self.score > self.highScore:
			self.highScore += 1
		self.update_score()

	def decrease_lives(self):
		self.lives -= 1
		self.update_score()

	def reset(self):
		self.clear()
		self.score = 0
		self.update_score()
		open('highestScore.txt', 'w').write(str(self.highScore))
