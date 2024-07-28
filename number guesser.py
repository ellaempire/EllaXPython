import random

randomize_number = input('please type a number: ')

if  randomize_number.isdigit:
    randomize_number = int(randomize_number)
    if randomize_number <= 0:
        print('please type a number larger than 0')
        quit()
else:
    print('please type a number later')
    quit()


random_number = random.randint(0,randomize_number)
guesses = 0

while True:
    guesses += 1
    user_pick = input('take a wild guess ')
    if user_pick.isdigit:
        user_pick = int(user_pick)
    else:
        print('type a number')
        continue 

    if user_pick == random_number:
        print('you got that correct')
        print('you got it in', guesses , 'guesses') 
        break
    else:
        print('thats incorrect')

   