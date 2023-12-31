import turtle as tr
from paddle import Paddle
from ball import Ball
from score import Score
from interface import Interface as I
from bricks import Bricks
import time

# Creating a black background
background = tr.Screen()
background.setup(width=1200, height=600)
background.bgcolor('black')
# Naming the turtle shell
background.title('Brick Breaker')
# Turn off automatic screen updates
background.tracer(0)

# Call the modules
Interface = I()
Interface.header()

score = Score(lives=4)
paddle = Paddle()
bricks = Bricks()
ball = Ball()

playing_game = True

# Use the left and right keys to move the paddle
background.listen()
background.onkey(key='Left', fun=paddle.move_left)
background.onkey(key='Right', fun=paddle.move_right)


# Use the pre-existing modules to check collision


def check_collision_with_walls():

	global ball, score, playing_game, Interface

	# Collision detection with left and right walls:
	if ball.xcor() < -580:
		ball.bounce(x_bounce=True, y_bounce=False)

	if ball.xcor() > 570:
		ball.bounce(x_bounce=True, y_bounce=False)
		return

	# collision detection with upper wall
	if ball.ycor() > 280:
		ball.bounce(x_bounce=False, y_bounce=True)
		return

	# Collision detection with bottom wall
	# In this case, the user fails to hit the ball thus he loses, and the game resets
	if ball.ycor() < -280:
		ball.reset()
		score.decrease_lives()
		if score.lives == 0:
			score.reset()
			playing_game = False
			Interface.game_over(win=False)
			return
		Interface.change_color()
		return


# Create boudaries for the paddle
def check_collision_between_paddle_wall():
	if paddle.xcor()>=520:
		paddle.setx(520)
	if paddle.xcor()<=-530:
		paddle.setx(-530)
	
def check_collision_with_paddle():

	global ball, paddle
	# record x-axis coordinates of ball and paddle
	paddle_x = paddle.xcor()
	ball_x = ball.xcor()

	# check if the ball's distance (from its middle) from the paddle (from its middle) is less than \
	# the width of the paddle and the ball is below a certain coordinate to detect their collision
	if ball.distance(paddle) < 110 and ball.ycor() < -250:

		# If Paddle is on Right of background
		if paddle_x > 0:
			if ball_x > paddle_x:
				# If ball hits paddles left side it
				# should go back to left
				
				ball.bounce(x_bounce=True, y_bounce=True)
				ball.sety(-260)
				return
			else:
				ball.bounce(x_bounce=False, y_bounce=True)
				ball.sety(-260)
				return

		# Elif Paddle is the left of the background
		elif paddle_x < 0:
			if ball_x < paddle_x:
				# If ball hits paddles left side it 
				# should go back to left
				ball.bounce(x_bounce=True, y_bounce=True)
				ball.sety(-260)
				return
			else:
				ball.bounce(x_bounce=False, y_bounce=True)
				ball.sety(-260)
				return

		# Else Paddle is in the middle horizontally
		else:
			if ball_x > paddle_x:
				ball.bounce(x_bounce=True, y_bounce=True)
				ball.sety(-260)
				return
			elif ball_x < paddle_x:
				ball.bounce(x_bounce=True, y_bounce=True)
				ball.sety(-260)
				return
			else:
				ball.bounce(x_bounce=False, y_bounce=True)
				ball.sety(-260)
				return


def check_collision_with_bricks():
	global ball, score, bricks

	for brick in bricks.bricks:
		if ball.distance(brick) < 35:
			score.increase_score()
			brick.quantity -= 1
			if brick.quantity == 0:
				brick.clear()
				brick.goto(3000, 3000)
				bricks.bricks.remove(brick)

			# detect collision from left
			if ball.xcor() < brick.left_wall:
				ball.bounce(x_bounce=True, y_bounce=False)

			# detect collision from right
			elif ball.xcor() > brick.right_wall:
				ball.bounce(x_bounce=True, y_bounce=False)

			# detect collision from bottom
			elif ball.ycor() < brick.bottom_wall:
				ball.bounce(x_bounce=False, y_bounce=True)

			# detect collision from top
			elif ball.ycor() > brick.upper_wall:
				ball.bounce(x_bounce=False, y_bounce=True)


# Ensure game runs correctly by running functions
while playing_game:

		# Update background with all the motion that has happened
		background.update()
		time.sleep(0.01)
		ball.move()

		check_collision_between_paddle_wall()
		# Wall collision detection
		check_collision_with_walls()

		# Paddle collision detection
		check_collision_with_paddle()

		# Brick collision detection
		check_collision_with_bricks()


		if len(bricks.bricks) == 0:
			Interface.game_over(win=True)
			break


tr.mainloop()
