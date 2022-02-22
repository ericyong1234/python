#터틀런 게임 II - 완성
import turtle as t
import random

score = 0
playing = False

te = t.Turtle()
te.shape("turtle")
te.speed(0)
te.color("red")
te.up()
te.goto(0, 200)


ts = t.Turtle()
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
def start():
    global playing  
    if playing == False:
        playing = True
        t.clear()
        play()
def play():
    global score
    global playing
    
    ang = te.towards(t.pos())
    te.setheading(ang)
    
    t.forward(10)
    te.forward(10)
    if t.distance(ts) < 12:
        score = score + 1
        t.write(score)
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        ts.goto(x, y)
    if t.distance(te) <12 :
        text = "Score : " + str(score)
        message("Game over", text)
        playing = False
        score = 0
    if playing:
        t.ontimer(play, 100)
        






def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center",("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center",("", 20))
    t.home()

t.title("Turtle Run")
t.setup(500, 500)
t.shape("turtle")
t.bgcolor("skyblue")
t.speed(0)
t.up()
t.color("gold")



t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start , "space")
t.listen()
start()








