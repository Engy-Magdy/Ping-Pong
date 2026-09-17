from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
import random
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title('Ping Pong Game')
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
from score import Score
r_score=Score((200,200))
l_score=Score((-200,200))


speed=0.1
game_on=True
while game_on:
    screen.update()
    time.sleep(speed)

    ball.goto(ball.xcor()+ball.x_move,ball.ycor()+ball.y_move)
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.y_move*=-1
        speed*=0.9
        
    if (ball.xcor()>=330 and ball.distance(r_paddle)<=50) or (ball.xcor()<=-330 and ball.distance(l_paddle)<=50):
         ball.x_move*=-1
         speed*=0.9
         
    if ball.xcor()>400:
        l_score.point()
        ball.goto(0,0)
        ball.x_move*=-1
        speed=0.1
    if ball.xcor()<-400:
        r_score.point()
        ball.goto(0,0)
        ball.x_move*=-1
        speed=0.1
    if l_score.score==10:
         game_on=False
         screen.clear()
         screen.bgcolor("darkred")
         message=Turtle()
         message.color("white")
         message.write("Left paddle wins!",font=("courier",30,"bold"),align="center")
         message.hideturtle()
    if r_score.score==10:
             game_on=False
             screen.clear()
             screen.bgcolor("darkred")
             message=Turtle()
             message.color("white")
             message.write("Right paddle wins!",font=("courier",30,"bold"),align="center")
             message.hideturtle()
screen.exitonclick()
        

    
