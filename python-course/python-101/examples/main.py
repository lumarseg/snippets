# Juego de Piedra, Papel y Tijera
import random

options=("rock", "paper", "scissor")
computer_wins = 0
user_wins = 0
round = 1

while True:
  print("*"*10)
  print("Round", round)
  print("*"*10)

  user_option = input(f"Hey, choose <{options[0]}>, <{options[1]}> or <{options[2]}>: ")
  user_option = user_option.lower()

  if not user_option in options:
    print("- Error: Invalid option")
    continue
  else:
    computer_option = random.choice(options)
    print("- User option:", user_option)
    print("- Computer option:", computer_option)

    if computer_option == user_option:
      print("- User ties.")
    elif computer_option == options[-1]:
      if user_option == options[-1+1]:
        print("- User Wins !!!")
        user_wins += 1
      elif user_option == options[-1-1]:
        print("- User Loses...")
        computer_wins += 1
    elif computer_option == options[0]:
      if user_option == options[0+1]:
        print("- User Wins !!!")
        user_wins += 1
      elif user_option == options[0-1]:
        print("- User Loses...")
        computer_wins += 1
    elif computer_option == options[1]:
      if user_option == options[1+1]:
        print("- User Wins !!!")
        user_wins += 1
      elif user_option == options[1-1]:
        print("- User Loses...")
        computer_wins += 1
    
    if computer_wins == 3:
      print("-"*10)
      print("Computer is Winner!!!")
      break
    if user_wins == 3:
      print("-"*10)
      print("User is Winner!!!")
      break
    
  round += 1


