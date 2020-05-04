import turtle
import os


y_change = 30

scorea = 0
scoreb = 0

win = turtle.Screen()
win.setup(800,600)
win.bgcolor("black")
win.title("Pong By Vikas")
win.tracer(0)

#paddlea
paddlea = turtle.Turtle()
paddlea.speed(0)
paddlea.color("white")
paddlea.shape("square")
paddlea.shapesize(5,1)
paddlea.penup()
paddlea.goto(-350,0)

#paddleb
paddleb = turtle.Turtle()
paddleb.speed(0)
paddleb.color("white")
paddleb.shape("square")
paddleb.shapesize(5,1)
paddleb.penup()
paddleb.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.shapesize()
ball.penup()
ball.goto(0,0)
balldx = 0.9
balldy = 0.9


pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1 score:0  Player2 score:0 ", align="center", font=("Courier",24,"normal",))


def paddlea_up():
	y = paddlea.ycor()
	y += y_change
	paddlea.sety(y)

def paddlea_down():
	y = paddlea.ycor()
	y -= y_change
	paddlea.sety(y)

def paddleb_up():
	y = paddleb.ycor()
	y += y_change
	paddleb.sety(y)

def paddleb_down():
	y = paddleb.ycor()
	y -= y_change
	paddleb.sety(y)


win.listen()
win.onkeypress(paddlea_up, "w")
win.onkeypress(paddlea_down, "s")
win.onkeypress(paddleb_up, "Up")
win.onkeypress(paddleb_down, "Down")

while True:
	win.update()

	ball.setx(ball.xcor() + balldx)
	ball.sety(ball.ycor() + balldy)


	if ball.ycor() > 290:
		ball.sety(290)
		balldy *= -1
	if ball.ycor() < -290:
		ball.sety(-290)
		balldy *= -1

	if ball.xcor() > 390:
		ball.goto(0,0)
		balldx *= -1
		scorea += 1
		pen.clear()
		pen.write(f"Player 1 score:{scorea}  Player2 score:{scoreb} ", align="center", font=("Courier",24,"normal",))

	if ball.xcor() < -390:
		ball.goto(0,0)
		balldy *= -1
		scoreb += 1
		pen.clear()
		pen.write(f"Player 1 score:{scorea}  Player2 score:{scoreb} ", align="center", font=("Courier",24,"normal",))



	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleb.ycor() + 40 and ball.ycor() > paddleb.ycor() - 40):
		ball.setx(340)
		balldx *= -1


	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddlea.ycor() + 40 and ball.ycor() > paddlea.ycor() - 40):
		ball.setx(-340)
		balldx *= -1

	if paddlea.ycor() + 40 < -200:
		paddlea.sety(-240)

	if paddlea.ycor() + 40 > 290:
		paddlea.sety(250)

	if paddleb.ycor() + 40 > 290:
		paddleb.sety(250)

	if paddleb.ycor() + 40 < -210:
		paddleb.sety(-250)

