import json

def add_expense(expenses, description, amount):
    expenses.append({'description': description, 'amount': amount})
    print(f'added expense: {description}, amount:  {amount}')

def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amount']
    return sum

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def budget_details(budget, expenses):
    print(f'Total Budget: {budget}')
    print('Expenses: ')
    for expense in expenses:
        print(f'- {expense['description']}: {expense['amount']}')
    print(f'Total Spent: {get_total_expenses(expenses)}')
    print(f'Remaining Budget: {get_balance(budget, expenses)}')

def load_budget_data(filepath):
    try:
        with open (filepath, 'r') as file:
            data = json.load(file)
            return data ['main_budget'], data['expenses']
    except (FileNotFoundError, json.JSONDecodeError):
        return 0,[]
    
def save_budget_data(filepath, main_budget, expenses):
    data = {
        'main_budget': main_budget,
        'expenses' : expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    

def main():
    print('welcome to budgetly')
    main_budget = float(input('please enter your main budget '))
    budget = main_budget
    expenses = []

    while True:
        print('\nwhat would you like to do? ')
        print('1. Add an expense')
        print('2. Show budget details')
        print('3.exit')
        choice = input('enter your choice (1/2/3) ')

        if choice == '1':
            description = input('enter your expense description ')
            amount = float(input('enter expense amount '))
            add_expense = (expenses, description, amount)
        elif choice == '2':
            budget_details = (budget, expenses)
        elif choice == '3':
            print('exiting budgetly, goodbye')
            break
        else:
            print('invalid option. please try again')

if __name__ == '__main__':
    main()