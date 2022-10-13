
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.shape("turtle")
def forward():
    t.fd(20)

def backward():
    t.bk(20)

def right():
    t.right(10)

def left():
    t.left(10)
screen.listen()
while True:
    screen.onkey(forward, 'w')
    screen.onkey(backward, 's')
    screen.onkey(right, 'd')
    screen.onkey(left, 'a')
    screen.onkey(t.reset, 'c')

    screen.exitonclick()
