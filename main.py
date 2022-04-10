from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

# set up main screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# #create paddle
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = Score()

# Move paddles
# right paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# left paddles
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision wit r paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    #   detect collision with r wall
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        score.update_scoreboard()

    #   detect collision with l wall
    if ball.xcor() < - 380:
        ball.reset_position()
        score.r_point()
        score.update_scoreboard()

# exit game on click

screen.exitonclick()
