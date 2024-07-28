name = input('before you proceed, what is your name? ')
print('welcome', name, 'to my adventure game! HAVE FUN!')
print('first pick an adventure')

#if youve come back to this, tweak it as well as you can plus you should have created a guideline for a mad adventure game

adventure = input('you have beeen walking and you reach a path. Do you want to go left or right? ').lower()
if adventure == 'left':
    task_a = input('you have now come to a river and you have to cross it, do you want to swim or use a canoe? ').lower()

elif adventure == 'right':
    print()

else:
    print('pick a damn bloody choice')