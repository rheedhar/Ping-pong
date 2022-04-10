from turtle import Turtle


# paddle class

class Paddle(Turtle):
    def __init__(self, xcorr, ycorr):
        super().__init__()
        self.xcorr = xcorr
        self.ycorr = ycorr
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.xcorr, self.ycorr)

    def go_up(self):
        y_coordinate = self.ycor() + 30
        self.goto(self.xcor(), y_coordinate)

    def go_down(self):
        y_coordinate = self.ycor() - 30
        self.goto(self.xcor(), y_coordinate)
