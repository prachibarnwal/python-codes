import turtle
import winsound
from pygame import mixer

 #SONG PLAYING
mixer.init()
mixer.music.load("song1.mp3")
mixer.music.set_volume(100.5) 
mixer.music.play()

# creating background screen
win = turtle.Screen()
win.setup(width=1200,height=600)
win.bgcolor('black')

# playing music
winsound.PlaySound('anthem.wav',winsound.SND_ASYNC)


# adding image
t = turtle.Turtle()
win.addshape('ind1.gif')
t.shape('ind1.gif')
t.shapesize(stretch_wid = 2, stretch_len = 2)

t.goto(-380,0)
# creating flag
stand = turtle.Turtle()
stand.color('white')
stand.shape('square')
stand.penup()
stand.setposition(-100,-280)
stand.pendown()
stand.goto(-100,280)

flag = turtle.Turtle()
flag.color('white')
flag.penup()
flag.setposition(-100,270)
flag.pendown()

length = 400
width = 80

def rect(color):
    flag.fillcolor(color)
    flag.begin_fill()
    flag.forward(length)
    flag.right(90)
    flag.forward(width)
    flag.right(90)
    flag.forward(length)
    flag.right(180)
    flag.end_fill()

rect('orange')
rect('white')
rect('green')

flag.left(90)
flag.forward(width*3)
flag.hideturtle()

# drawing wheel
wheel = turtle.Turtle()
wheel.color('blue')
wheel.penup()
wheel.width(2)
wheel.goto(100,107)
wheel.pendown()
wheel.circle(42)
wheel.penup()
wheel.goto(100,150)
wheel.pendown()
for i in range(26):
    wheel.forward(42)
    wheel.backward(42)
    wheel.right(13.8)


# writing text
text = turtle.Turtle()
text.hideturtle()
text.speed(2)

def write(message,pos,color):
    x,y = pos
    text.color(color)
    text.penup()
    text.goto(x,y)
    text.pendown()
    style = ('Courier',40,'italic')
    text.write(message,font=style)

#गणतंत्र दिवस की हार्दिक शुभकामनाएँ! 
write('गणतंत्र ',(80,-100),'orange')
write('दिवस  ',(10,-160),'white')
write('की  ',(142,-160),'blue')
write('हार्दिक ',(220,-160),'white')
write('शुभकामनाएँ! ',(60,-220),'green')

#song stop
mixer.music.stop()
turtle.done()
