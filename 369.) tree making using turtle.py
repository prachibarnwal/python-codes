import turtle
from pygame import mixer

#SONG PLAYING
mixer.init()
mixer.music.load("prachimusic123.mp3")
mixer.music.set_volume(100.5)
mixer.music.play()

t = turtle.Turtle()
ck = turtle.Screen()
ck.title("WLCM BACK MAMJI 🥳🥳")


t.screen.bgcolor("BLACK")
t.pensize(2)
t.color("GREEN")
t.left(90)
t.backward(100)
t.speed(200)
t.shape('turtle')
def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color("ORANGE")
        t.circle(2)
        t.color("BROWN")
        t.left(30)
        tree(3 * i/4)
        t.right(60)
        tree(3 * i / 4)
        t.left(30)
        t.backward(i)
tree(100)
mixer.music.stop()
turtle.done()
