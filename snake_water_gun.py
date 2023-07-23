import random

choices = ["Snake", "Water", "Gun"]
# snake_wins = choices[0] > choices[1]
# water_wins = choices[1] > choices[2]
# gun_wins = choices[2] > choices[1]
user_score = 0
computer_score = 0
draw = 0


def user_input():
    print("0 for Snake, 1 for Water, 2 for Gun ")
    user_choice = int(input("Enter your choice: "))
    # print(user_choice)
    if (user_choice == 0):
        print(choices[0])
        user_choice = choices[0]
        # print(user_choice)
    elif (user_choice == 1):
        print(choices[1])
        user_choice = choices[1]
    elif (user_choice == 2):
        print(choices[2])
        user_choice = choices[2]
    else:
        print("Invalid Input")
    # computer_input()
    return user_choice


def computer_input():
    computer_choice = random.choice(choices)
    print(computer_choice)

    # winner(user_choice, computer_choice)
    return computer_choice


def winner(user_choice, computer_choice):
    # choices = ["Snake", "Water", "Gun"]
    # if(snake_wins):
    # global user_score, computer_score, draw
    if (choices.index(user_choice) == choices.index(computer_choice)):
        # print("Draw")
        # draw += 1
        return -1

    elif (choices.index(user_choice) == choices.index(choices[0]) and choices.index(computer_choice) == choices.index(choices[1])):
        # if (choices.index(computer_choice) == choices.index(choices[1])):
        # print("You Win!!")
        # user_score += 1
        return 0
        # elif (choices.index(computer_choice) == choices.index(choices[2])):
        #     # print("Computer Wins!!")
        #     # computer_score += 1
        #     return 1

    elif (choices.index(user_choice) == choices.index(choices[1]) and choices.index(computer_choice) == choices.index(choices[2])):
        # if (choices.index(computer_choice) == choices.index(choices[2])):
        # print("You Win!!")
        # user_score += 1
        return 0
        # elif (choices.index(computer_choice) == choices.index(choices[0])):
        #     # print("Computer Wins!!")
        #     # computer_score += 1
        #     return 1

    elif (choices.index(user_choice) == choices.index(choices[2]) and choices.index(computer_choice) == choices.index(choices[0])):
        # if (choices.index(computer_choice) == choices.index(choices[0])):
        # print("You Win!!")
        # user_score += 1
        return 0
        # elif (choices.index(computer_choice) == choices.index(choices[1])):
        #     # print("Computer Wins!!")
        #     # computer_score += 1
        #     return 1
    else:
        return 1


start = input("Start Game(y/n): ")
while (start == 'y'):
    x = user_input()
    y = computer_input()
    a = winner(x, y)
    if (a == 0):
        print("You Win!!")
        user_score += 1
    elif (a == 1):
        print("Computer Win!!")
        computer_score += 1
    else:
        print("Draw")
        draw += 1
    start = input("Do you want to continue(y/n): ")
    # if(play_again==y):
    #     start="y"
    # else:
    #     start="n"

else:
    print("Your Score:",user_score, "Computer Score:",computer_score, "Draw:",draw)
