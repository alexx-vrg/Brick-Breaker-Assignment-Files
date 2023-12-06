"""import turtle
from turtle import Turtle

#we start by setting the move distance outside of the class indent
move_dist = 10

class Ball(Turtle):
    def __init__(ball):
        super().__init__() #we want to retrieve all properties from the master class so we use the super() function, and intit() applies is to the ball
        ball.shape('circle') #set the shape of the ball to a circle
        ball.colour('white') #set the colour of the ball to white bc the screen bg colour is black

#because the screen is set on a x,y space, we need to define the movement of the ball according to the x and y axis:
        ball.move_dist_x = move_dist
        ball.move_dist_y = move_dist #the moving distance on both x and y every time the ball moves is 10 steps
        ball.goto(-50, 300) #we set the INITIAL POSITION of the ball (change selon screen)
        ball.reset() #the ball is ready to be in the game

#we start a new block for speed and movement of the block once the game has started:
    def movement(ball):     
        ball.move_speed = 0.05 #we set the speed at which the ball will move
#we need to define the movement of the ball according to the x and y axis
        ball.movement = ball.move_dist_x + ball.move_dist_y


#we start a new block to study the case in which the ball bounces on a brick, on a boundary/wall, or on the paddle:
        def bounce(ball, x_bounce, y_bounce):
       #we start an if loop for if the ball meets an object:
                if x_bounce:
                     ball.move_dist_x *=-1
                elif y_bounce:
                      ball.move_dist_y *=-1
        
#we start a new block to reset the ball's position every time the game starts or restarts:
        def reset(ball):
             ball.goto(x= 50, y= 820)
             ball.move_dist_y = 10"""
        
import turtle
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()  
        self.shape('circle')
        self.penup()
        self.color('white')  # Set the color to white
        self.goto(0, -150)
        self.move_dist_x = 10
        self.move_dist_y = 10
        self.move_speed = 0.05

    def movement(self):
        # Move the ball according to the x and y axis
        new_x = self.xcor() + self.move_dist_x
        new_y = self.ycor() + self.move_dist_y
        self.goto(new_x, new_y)

    def reset_position(self):
        # Reset the ball's position to the initial position
        self.goto(-50, 300)

    def start(self):
        # Add any initialization logic needed when the game starts or restarts
        pass
