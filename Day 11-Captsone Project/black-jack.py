from logo import logo
import random

import os

os_clear = 'cls' if os.name == 'nt' else 'clear'

def check_winner(cards_player, cards_comp, end_game = False):
    """Get the player_cards and comp_cards  
    Show the winner if deal_more is False"""
    player_score = sum(cards_player)
    comp_score = sum(cards_comp)



    if player_score > 21:
        print(f"\t Your final hand: {cards_player}, final score: {player_score}")
        print(f"\t Computer's final hand: {cards_comp}, final_score: {comp_score}")

        print("You went over. You lose 🤬")
        return False
    elif comp_score > 21:
        print("Compter went over. You win 🤬")
        return False
    elif end_game:
        if player_score > comp_score:
            print("Shit! You win")
        else:
            print("Computer wins")

        return False
    
    return True

    # print(f"\t You cards: {cards_player}, current score: {player_score}")
    # print(f"\t Computer's cards: {cards_player}, current score: {player_score}")

def play(cards, cards_player = [], cards_comp = []):
    # can_continue = True
    cards_player.append(random.choice(cards))
    print(f"\t Your cards: {cards_player}, current score: {sum(cards_player)}")
    
    cards_comp.append(random.choice(cards))
    print(f"\t Computer's first card: {cards_comp[0]}")

    can_continue = check_winner(cards_player, cards_comp)

    if can_continue:
        deal_more = input("Type 'y' to get another card, type 'n' to pass: ")
        if deal_more == 'y':
            play(cards, cards_player, cards_comp)

        else:
            check_winner(cards_player, cards_comp, end_game=True)
            start_new = input("Type 'y' to start a new game,  type 'n' to exit: ")
            if start_new == 'y':
                main()
            else:
                return
    return


def main():
    os.system(os_clear)
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_player = random.choices(cards,k=1)
    # cards_comp = random.choices(cards, k=1)
    play(cards, cards_player)
    
if __name__ == "__main__":
    play_game = input("Do you want to play a game of blackjack? 'y' or 'n'? ").lower()
    if play_game:
        main()
        


