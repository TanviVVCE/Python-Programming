from random import choice

users_choice = input("Enter your choice: \n")
options_to_select = ['rock', 'paper', 'scirrors']
computers_choice = choice(options_to_select)
print(f'Users choice is {users_choice}')
print(f'Computers Choice is {computers_choice}')

if (users_choice):
    if ((users_choice == 'rock' and computers_choice == 'paper') or (users_choice == 'paper' and computers_choice == 'scissors') or (users_choice == 'scissors' and computers_choice == 'rock')):
        print('Computer wins')
    else:
        if (users_choice == computers_choice):
            print('Better luck next time !!')
        else:
            print('You Win')
else:
    print('Enter a valid choice')
