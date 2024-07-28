print("welcome to my bloody quiz!")

playing = input("are you ready to play? ")
print(playing)

if playing.lower() == "yes":
    print("in 3,2,1 Let's Begin!!")
    score = 0
else:
    print("okay then, bye bye")
    quit()

question = input('how long does it take to counter a security breach? ')

if question == "240 days":
    print('Correct')
    score += 1
else:
    print('incorect! lets see how you do in number 2')

question = input('what is the full meaning of ECOWAS? ')

if question.lower() == "economic community of west african states":
    print('Correct')
    score += 1 
else:
    print('incorect! lets see how you do in number 3')

question = input('who is a major proponent of systems theory? ')

if question.lower() == "david easton":
    print('Correct')
    score += 1
else:
    print('incorect! lets see how you do in number 4')

question = input('what is the full meaning of GDSC? ')

if question.lower() == "google developers student club":
    print('Correct')
    score += 1 
else:
    print('incorect! lets see how you do in number 5')

print('finally, you got ' + str(score) +  ' questions correct')