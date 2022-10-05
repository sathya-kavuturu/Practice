from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

    
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' :").lower()
if difficulty=='easy':
    attempts =10
elif difficulty=='hard':
    attempts=5
    
print(f"You have {attempts} attempts remaining to guess the number.")
is_game_over = False
while not is_game_over:
    answer = random.randint(1, 101)
    guessed = int(input("Make a Guess: "))
    attempts -=1
    if guessed ==  answer:
        print("You won!")
        is_game_over =True
    elif guessed > answer:
        print("Too high.")
    elif guessed < answer:
        print("Too low.")
    
    if attempts==0:
        print("you Lose!")
        is_game_over = True
        break
    print("Guess Again. ")
    print(f"You have {attempts} attempts remaining to guess the number.")
    
        
        
        
    