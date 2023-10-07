# Juego de Piedra, Papel y Tijera
import random


def choose_options(elements, round):

    print("*"*10)
    print("Round", round)
    print("*"*10)

    user_option = input(
        f"Hey, choose <{elements[0]}>, <{elements[1]}> or <{elements[2]}>: ")
    user_option = user_option.lower()

    if not user_option in elements:
        print("- Error: Invalid option, try again...")
        return None, None
    else:
        computer_option = random.choice(elements)
        print("- User option:", user_option)
        print("- Computer option:", computer_option)
        return user_option, computer_option


def evaluate_options(elements, options, user_wins, computer_wins):
    user_option = options[0]
    computer_option = options[1]

    if computer_option == user_option:
        print("- User ties.")
    elif computer_option == elements[-1]:
        if user_option == elements[-1+1]:
            print("- User Wins !!!")
            user_wins += 1
        elif user_option == elements[-1-1]:
            print("- User Loses...")
            computer_wins += 1
    elif computer_option == elements[0]:
        if user_option == elements[0+1]:
            print("- User Wins !!!")
            user_wins += 1
        elif user_option == elements[0-1]:
            print("- User Loses...")
            computer_wins += 1
    elif computer_option == elements[1]:
        if user_option == elements[1+1]:
            print("- User Wins !!!")
            user_wins += 1
        elif user_option == elements[1-1]:
            print("- User Loses...")
            computer_wins += 1
    return user_wins, computer_wins


def check_results(user_wins, computer_wins, gameover):

    if computer_wins == 3:
        print("-"*10)
        print("Computer is Winner!!!")
        gameover = True

    if user_wins == 3:
        print("-"*10)
        print("User is Winner!!!")
        gameover = True
    return gameover


def run_game():
    computer_wins = 0
    user_wins = 0
    round = 1
    elements = ("rock", "paper", "scissor")
    gameover = False

    while True:
        if gameover == True:
            break

        options = choose_options(elements, round)

        if options[0] == None:
            continue

        else:
            user_wins, computer_wins = evaluate_options(
                elements, options, user_wins, computer_wins)
            round += 1
            gameover = check_results(user_wins, computer_wins, gameover)


run_game()
