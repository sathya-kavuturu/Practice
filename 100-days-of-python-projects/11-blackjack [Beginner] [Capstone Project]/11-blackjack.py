from art import logo
import os
import random
 
if input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")=='y':
    print(logo)
    
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards)==21 and cards==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

is_game_over=False


user =[]
computer=[]
for i in range(2):
    user.append(deal_card())
    print(user[i])
    computer.append(deal_card())
    print(computer[i])
    

while not is_game_over:
    user_score = calculate_score(user)
    computer_score = calculate_score(computer)
    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Comuter's first card: {computer[0]}")

    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over = True
    else:
        choose = input("Type 'y' to get another card, type 'n' to pass: ")
        if choose=='y':
            user.append(deal_card())
        else:
            is_game_over=True


while computer_score!=0 and computer_score<17:
    computer.append(deal_card())
    computer_score = calculate_score(computer)  
    
    
    
    
    
    
    


    

