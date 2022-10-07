from art import logo,vs
from game_data import data
import random
import os

def compare(op1, op2):
    if op1['follower_count'] > op2['follower_count']:
        return 'a'
    else:
        return 'b'


option1= random.choice(data)
option2 = random.choice(data)
if option1 == option2:
    option2 = random.choice(data)
score = 0

while True:
    print(logo)
    print(f"Compare A: {option1['name']}, {option1['description']}, {option1['country']}. ")
    print(vs)
    print(f"Compare B: {option2['name']}, {option2['description']}, {option2['country']}. ")

    answer = compare(option1, option2)
    if input("Who has more followers? Type 'A' or 'B': ").lower() == answer:
        score +=1
        option1 = option2
        option2 = random.choice(data)
        os.system('cls')
    else:
        print(f"Sorry, that's wrong!  Final Score: {score}")
        break

