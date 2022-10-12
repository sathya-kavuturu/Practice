###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
import turtle as t

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

tim = t.Turtle()
t.colormode(255)
tim.speed(("fastest"))
tim.up()
tim.hideturtle()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)
num_dots = 100
for dot_count in range(1, num_dots+1):
    tim.dot(20, random.choice(rgb_colors) )
    tim.fd(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)















screen = t.Screen()
screen.exitonclick()