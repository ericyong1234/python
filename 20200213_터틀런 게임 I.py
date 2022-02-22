#터틀런 게임 I

import turtle as t
import random

te = t.Turtle()             #악당 거북이
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

tr = t.Turtle()
tr.shape("turtle")
tr.color("red")
tr.speed(0)
tr.up()
tr.goto(0, -100)

ts = t.Turtle()             #목표
ts.shape("circle")
ts.color("purple")
ts.speed(0)
ts.up()
ts.goto(0, -200)


def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def play():
    t.forward(20)
    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(1)
    tr.setheading(ang)
    tr.forward(1)

    if t.distance(te) >= 12 :
        t.ontimer(play, 100)

    if t.distance(tr) >= 10:
        t.ontimer(play, 100)

    if t.distance(ts) < 12 :
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        ts.goto(x, y)
    

t.setup(850, 850)
t.bgcolor("skyblue")
t.shape("turtle")
t.speed(0)
t.up()
t.color("gold")

t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.listen()
play()



