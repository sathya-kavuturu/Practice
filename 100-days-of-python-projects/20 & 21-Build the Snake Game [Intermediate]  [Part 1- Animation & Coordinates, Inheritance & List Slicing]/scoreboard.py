from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.print_score()
        
    def print_score(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        
        