# from turtle import *
#
# sample = Turtle()
# my_screen = Screen()
# print(my_screen.canvheight)
# sample.shape("turtle")
# sample.color("red","yellow")
# sample.fd(100)
# my_screen.exitonclick()

from prettytable import *

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "l"
print(table)
