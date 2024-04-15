# from random import randint

# computer_number = randint(1, 10)
# user_number = input('Guess a number between 1 to 10 : ')
# user_number = int(user_number)

# while computer_number != user_number:
#     if (computer_number > user_number):
#         print('Too low, guess something higher')
#         user_number = int(input('Guess a number between 1 to 10 : '))
#     elif (computer_number < user_number):
#         print('Too high, guess something lower')
#         user_number = int(input('Guess a number between 1 to 10 : '))
# print('You guessed it , you win')

# from random import randint

# random_number = randint(1, 10)
# guess = None

# while True:
#     guess = input('Guess number between 1 to 10 : ')
#     guess = int(guess)
#     if (guess > random_number):
#         print('Too high guess something lower!')
#     elif (guess < random_number):
#         print('too low')
#     else:
#         print('you won')
#         choice = input('wanna play ')
#         if (choice == 'y'):
#             random_number = randint(1, 10)
#             guess = None
#         else:
#             print('Thanks for playing')
#             break

# rock paper scissors using for loop

from random import choice
player_wins = 0
computer_wins = 0
while player_wins <= 2 or computer_wins <= 2:
    print(
        f'Computer wins : {computer_wins} \/\/\/ Player wins : {player_wins}')
    users_choice = input("Enter your choice: \n")
    options_to_select = ['rock', 'paper', 'scirrors']
    computers_choice = choice(options_to_select)
    print(f'Users choice is {users_choice}')
    print(f'Computers Choice is {computers_choice}')

    if (users_choice):
        if ((users_choice == 'rock' and computers_choice == 'paper') or (users_choice == 'paper' and computers_choice == 'scirrors') or (users_choice == 'scirrors' and computers_choice == 'rock')):
            print('Computer wins')
            computer_wins += 1
        else:
            if (users_choice == computers_choice):
                print('Better luck next time !!')
                computer_wins += 1
                player_wins += 1
            else:
                print('You Win')
                player_wins += 1
    else:
        print('Enter a valid choice')
