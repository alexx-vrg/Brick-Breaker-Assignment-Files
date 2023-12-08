from turtle import Turtle

#set up the move distance of the paddle as well as its boundaries
MOVE_DIST = 50
LEFT_BOUNDARY = -800
RIGHT_BOUNDARY = 800

class Paddle(Turtle):

#define the paddle's length, color and shape
    def __init__(self):
        super().__init__()
        self.color('steel blue')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(x=0, y=-280)

# Register key events
        self.screen.listen()
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")

#set it to move to the left
    def move_left(self):
        new_x = self.xcor() - MOVE_DIST
        if new_x > LEFT_BOUNDARY:
            self.goto(new_x, self.ycor())

#set it to move to the right
    def move_right(self):
        new_x = self.xcor() + MOVE_DIST
        if new_x < RIGHT_BOUNDARY:
            self.goto(new_x, self.ycor())

#make the movement continue if the key is still being pressed
    def continuous_move(self):
        # Check if the left or right key is held down, and move accordingly
        if self.screen.iskeypressed("Left"):
            self.move_left()
        if self.screen.iskeypressed("Right"):
            self.move_right()

        # Schedule the continuous_move method to run again after a short delay
        self.screen.ontimer(self.continuous_move, 50)
