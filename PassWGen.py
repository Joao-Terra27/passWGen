from functs import dados, user
from time import sleep

while True:
    print(dados.senha())
    print()

    print('Wich password do you want to use? [1 ~ 5]')
    print(user.usuario())
    
    resp = ' '
    while resp not in 'YN':
        print('\nDo you wish generate another password? [Y/N]')
        resp = input('>>> ').strip().upper()[0]
        
    if resp == 'S':
        print(dados.senha())
        print('\nChoose another password [1 ~ 5]')
        print(user.usuario())
    
    elif resp == 'N':
        print('\nOkay, thanks! Bye...')
        sleep(1)
        
        break