from turtle import Turtle

MOVE_DIST = 10 #we set the distance the ball moves each time before the loops


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape('circle') #give the ball characteristics:
		self.color('white') 
		self.penup()
		self.x_move_dist = MOVE_DIST
		self.y_move_dist = MOVE_DIST
		self.reset()

	def move(self):
		new_y = self.ycor() + self.y_move_dist #for x and y, the ball moves to new coordinates by a certain distance, defined above
		new_x = self.xcor() + self.x_move_dist
		self.goto(x=new_x, y=new_y)

	def bounce(self, x_bounce, y_bounce): 
		if x_bounce:
			self.x_move_dist *= -1 #when the ball meets an obstacle, its direction is reversed, so -1

		if y_bounce:
			self.y_move_dist *= -1

	def reset(self):
		self.goto(x=0, y=-240) #we reset the position
		self.y_move_dist = 10 #and the moving distance, for when the user loses
