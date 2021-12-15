from logo import logo, vs
from data import data
from random import choice


# get two datas
def get_datas():
    """
    return two randomly selected datas
    """
    d1 = choice(data)
    d2 = choice(data)
    return d1, d2

# print(get_datas())

# show one and hide the follower count of the other
def show_datas(d1, d2, game_on= True):
    """
    takes two datas \n
    if game_on is True (default) doesn't show the follower_count of the 2nd data \n
    else shows the follower_count of the 2nd data
    """

    d2_copy = d2.copy()
    for key,value in d1.items():
        print(f"{key.capitalize()}: {str(value).capitalize()}")

    print(vs)

    if game_on:
        del(d2_copy['follower_count'])

    for key,value in d2_copy.items():
        print(f"{key.capitalize()}: {str(value).capitalize()}")

def guess_correct(d1, d2, score, guess):
    """
    takes two scores and calculate the score \n
    if 2nd is higher returns score and True \n
    else returns score and False
    """
    d1_score = d1['follower_count']
    d2_score = d2['follower_count']

    game_on = True
    if d1_score < d2_score and guess == 'h' or d2_score < d1_score and guess == 'l':
        score += 1
    else:
        game_on = False

    return score, game_on

def game():
    score = 0
    game_on = True
    while game_on:
        d1, d2 = get_datas()
        # show_datas(*get_datas())
        show_datas(d1, d2)

        # ask the user if the follower count of the other is higher or lower

        guess = input("\nSo is the follower count is higher or lower:\n \t'h' for higher \n \t'l' for lower\n")

        # if the guess was right up the score else end the game and 
        score, game_on = guess_correct(d1, d2, score, guess)
        # print(score, game_on)
        print(f"Your score: {score}")

    # print the score of the user
    print("The correct data's are:")
    show_datas(d1, d2, game_on)


# ask the user if they want to start the game again 
while True:
    play_game = input("\nPlay Game: \n \t'y': 'yes' \n \t'n': 'no' \n").lower()
    if play_game == 'y':
        game()