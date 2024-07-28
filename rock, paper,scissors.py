import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('please type rock/paper/scissors to continue or Q to quit: ').lower()
    if user_input == 'q':
        quit()
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    computer_guesses = options[random_number]
    print('computer picked', computer_guesses, '.')

    if user_input == "rock" and computer_guesses == 'scissors':
        print('oh shit, you won')
        user_wins += 1
         
#when you come back to this, remember to input the win conditions using the elif statement
    else:
        print('computer winns')
        computer_wins += 1

print('you won', user_wins, 'times')
print ('computer won', computer_wins, 'times')
print('akay byee')