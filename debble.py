from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(5,1)
    def go_up(self) :
        self.goto(self.xcor(),self.ycor()+40)  
    def go_down(self) :
        self.goto(self.xcor(),self.ycor()-40)    