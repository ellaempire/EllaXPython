#to create this type of quiz game, i had to create a dictionary first. it consists of a proompt i.e question, option and nswer

#input questions later

questions =[
    {
        'prompt': '',
        'options': [''],
        'answer': ''
    }
]

#next, write out the functions. seems easier

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
            answer = input('A, B, C, D:  ').upper( )
            if answer == question['answer']:
                print('Correct \n')
                score += 1
            else:
                print('wrong. The correct answer was', question['answer'], '\n')

print('you got', str('score') , 'questions correct')       

run_quiz(questions)