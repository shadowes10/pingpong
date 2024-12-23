from turtle import Turtle,Screen
from debble import Paddle
from boll import Boll
import time
from scor import Scorbord

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Octucode: ping pong")
screen.tracer(0)

r_debble=Paddle((360,0))
l_debble=Paddle((-360,0))
boll=Boll()
scorbord=Scorbord()

screen.listen()
screen.onkey(r_debble.go_up,"Up")
screen.onkey(r_debble.go_down,"Down")
screen.onkey(l_debble.go_up,"w")
screen.onkey(l_debble.go_down,"s")

defald_sleep=0.1

game_on=True
while game_on:
    screen.update()
    time.sleep(defald_sleep)
    boll.goto(boll.xcor()+boll.x_move, boll.ycor()+boll.y_move)
    if boll.ycor()>=280 or boll.ycor()<=-280:
        boll.y_move*=-1
          
    if (boll.xcor()>=340 and boll.distance(r_debble)<=50) or (boll.xcor()<=-340 and boll.distance(l_debble)<=50):
        boll.x_move*=-1
        defald_sleep*.1
    #جه اليمين
    if boll.xcor()>=400 :
        boll.goto(0,0)
        boll.x_move*=-1
        defald_sleep=.1
        scorbord.l_point()

    #جه اليسار    
    if  boll.xcor()<=-400:
        boll.goto(0,0)
        boll.x_move*=-1
        defald_sleep=.1
        scorbord.r_point()        
   



screen.exitonclick()