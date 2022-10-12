#####Turtle Intro######
#import turtle
# import turtle as t
#
# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)

import turtle as t
tim = t.Turtle()
tim.shape("turtle")

######## Challenge 1 - Draw a Square ############

# tim.shape("turtle")
# tim.color("blue")
# for i in range(4):
#     tim.fd(100)
#     tim.right(90)



########### Challenge 2 - Draw a Dashed Line ########

# for _ in range(15):
#     tim.fd(10)
#     tim.up()
#     tim.fd(10)
#     tim.down()



########### Challenge 3 - Draw Shapes ########

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.fd(100)
#         tim.right(angle)
#
# for loop in range(3,10):
#     draw_shape(loop)



########### Challenge 4 - Random Walk ########
# import random
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     color = (r,g,b)
#     return color
#
#
# direction = [0,90,180,270]
# tim.speed(10)
# tim.width(10)
# for _ in range(200):
#     tim.color(random_color())
#     tim.fd(20)
#     tim.setheading((random.choice(direction)))



########### Challenge 5 - Spirograph ########
import random

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph((5))
screen = t.Screen()
screen.exitonclick()

