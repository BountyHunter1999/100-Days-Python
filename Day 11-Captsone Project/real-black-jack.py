import random 
import os

from logo import logo

os_clear = "cls" if os.name == "nt" else "clear"

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    cards_sum = sum(cards)
    if cards_sum == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and cards_sum > 21:
        # it seems not all instances of 11 are to be changed
        # cards = [ 1 if card == 11 else card for card in cards ]     
        cards.remove(11)
        cards.append(1)
        cards_sum = sum(cards)
    return cards_sum

def compare(p_score, c_score):
    """Compare the player scores and computer scores to decide who won the match or it's a draw"""
    if p_score == c_score:
        return "DRAW"
    elif c_score == 0:
        return "Computer Wins, she has BlackJack"
    elif p_score == 0:
        return "Player Wins with BlackJack"
    elif c_score > 21:
        return "Player Wins, Computer Went Over"
    elif p_score > 21:
        return "Computer Wins, You Went Over"
    elif p_score > c_score:
        return "Player Wins"
    else:
        return "Computer Wins"

def play_game():
    user_cards= [deal_card() for _ in range(2)]
    comp_cards= [deal_card() for _ in range(2)]


    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)


    is_game_over = False
    while not is_game_over:
        print(f"\t Your cards: {user_cards}, current score: {user_score}")

        print(f"\t Computer's first card: {comp_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score >= 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

            if user_should_deal == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True
        

    while comp_score < 17 and comp_score != 0:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"\t Your final hand: {user_cards}, final score: {user_score}")
    print(f"\t Computer's final hand: {comp_cards}, final_score: {comp_score}")

    print(compare(user_score, comp_score))


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you want to play a game of blackjack? 'y' or 'n'? ") == "y":
    os.system(os_clear)
    print(logo)
    play_game()