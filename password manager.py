print('before we begin, you have to give me a master password')
master_password = input('what is the master password? ')

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())

            


#'with' is used to open a file that allows you to carry out indentation.
#'with' also helps you to close the file. i can open a file with "file = open but i have to manually close the file with file.close"
# there a bunch of different modes in using a file; W which stands for write: to create a new file or override an existing  file i.e 
#if an existing file is open, W helps to wipe out the existing file and create a new one entirely.
# R is for read mode
# A is append mode which helps to add stuff to the end of an existing file and help create a new file if said file does not exist
# \n tells the txt editor to go to the next line 
#in order for me to splt the characters from the code, use data.split
#user, passw = data.split('|')
 #print ('user:', user, '|', 'password:', passw )

        
def add():
    name = input('account name ')
    password = input('password: ')
    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + password + '\n')

#ask them if they want to enter a new password or view their passwords

while True:
    mode = input('do you want to add a new password or view your saved passwords? view or add? if neither, press q to quit ').lower()
    if mode == 'q':
        break
    if mode == 'add':
        add() 
    elif mode == 'view':
        view()
    else:
        print('invalid option')
        continue


#ella you have to encrypt this