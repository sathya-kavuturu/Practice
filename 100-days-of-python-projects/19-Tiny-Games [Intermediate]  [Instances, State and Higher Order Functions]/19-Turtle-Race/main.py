from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-80, -50, -20, 10, 40, 70]
all_turtles=[]
is_race_on = True

for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(new_turtle)

while is_race_on:
    
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner.")
            else:
                print(f"You've lost! The {winning_color} is the winner.")
        
        random_movement = random.randint(0,10)
        turtle.fd(random_movement)
    



screen.exitonclick()