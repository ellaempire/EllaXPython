import random

words = ['tomatoes', 'watermelons', 'westphalia', 'barricades', 'ruby']
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 8

print('welcome to hangman')
#the code below means that if the attempts are greater than zero and there are still _s in the word display,
#then a new line should be printed and added in word display

while attempts > 0 and '_' in word_display: 
    print('\n' + '  '.join(word_display))
    guess = input('guess a letter ').lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess #if the guessed word is in the word display, then the index is replaced by the letter that was guessed thus revealing the letter
    else:
        print('that letter is not in the chosen word. try again')
        attempts -= 1          
        #the above code explains that if the user guesses a letter and the letter that has been guessed is in a chosen word, then the index of the chosen word would be replaced by the guessed word hence,enumerate

if '_' not in word_display:
        print('colderrrrr')
        print(' ' .join(word_display))
        print('you survived')
else:
     print('you run out of attempts. the word was:' + chosen_word)
     print('you lost')