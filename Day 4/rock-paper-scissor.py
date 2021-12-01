import random


print("--------WELCOME TO ROCK, PAPER, SCISSORS!------------")
choice = input("What do you choose? Type 0, for Rock, 1 for Paper or 2 for Scissors:")

com_choice = random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = {
    "0": rock,
    "1": paper,
    "2": scissors,
}

def win(p_choice, c_choice):
    p_choice = int(p_choice)
    c_choice = int(c_choice)
    # Player throws Rock
    # if p_choice == 0 and c_choice == 1:
    #     print("Computer wins with Paper")
    # elif p_choice == 0 and c_choice == 0:
    #     print("DRAW!!")
    # elif p_choice == 0 and c_choice == 2:
    #     print("Player wins with rock")

    # Player throws Paper
    # elif p_choice == 1 and c_choice == 1:
    #     print("DRAW!!")
    # elif p_choice == 1 and c_choice == 0:
    #     print("Player wins with Paper")
    # elif p_choice == 1 and c_choice == 2:
    #     print("Computer wins with Scissors")

    # Player throws Scissors
    # elif p_choice == 2 and c_choice == 1:
    #     print("Players wins with Scissors")
    # elif p_choice == 2 and c_choice == 0:
    #     print("Computer wins with rock")
    # elif p_choice == 2 and c_choice == 2:
    #     print("DRAW!!")

    # Better Logic
    if p_choice == 0 and c_choice == 2:
        print("You win!!")
    elif c_choice == 0 and p_choice == 2:
        print("You Lose!!")
    elif p_choice < c_choice:
        print("You Lose!!")
    elif p_choice > c_choice:
        print("You win!!")
    elif p_choice == c_choice:
        print("DRAW!!")

if int(choice) not in [0,1,2]:
    print("Invalid Input Select the appropriate number") 
else:
    print("You threw: \n", images[choice])
    print()
    print("Computer threw: \n", images[str(com_choice)])
    win(choice, com_choice)