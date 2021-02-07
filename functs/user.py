from time import sleep
from functs import dados

def usuario():
    user = int(input(' \33[1;34m>>>\33[m '))
    sleep(1)
    if user == 1:
        return f'Done! Your new pass word is {dados.data[user-1]}'
        
    elif user == 2:
        return f'Done! Your new pass word is {dados.data[user-1]}'

    elif user == 3:
        return f'Done! Your new pass word is {dados.data[user-1]}'

    elif user == 4:
        return f'Done! Your new pass word is {dados.data[user-1]}'

    elif user == 5:
        return f'Done! Your new pass word is {dados.data[user-1]}'
        
    else:
        return 'ERROR! Invalid value... please put a INTEGER value between 1 and 5.' 