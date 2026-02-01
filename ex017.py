import random

while True:
    resposta = input("rodar o dado : (y/n)").lower()
    if resposta == "y":
        dado1 = random.randint(1,6 )
        dado2 = random.randint(1,6 )
        print(f'({dado1}, {dado2}))')
    elif resposta == 'n':
        print('thanks for playing!')
        break
    else :
        print('invalid choice')



