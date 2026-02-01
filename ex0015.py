import random

print('bem vindo ao meu jogo de adivinhacao ')

numero_de_teto = input('digite o numero teto do desafio :')

if numero_de_teto.isdigit():
    numero_de_teto = int(numero_de_teto)
else :
    print('porfavor digite um numero inteiro')
    quit()
randor_number = random.randint(0, numero_de_teto)

numero_escolhido = None
tentativas = 0

while numero_escolhido != randor_number:
    tentativas += 1

    numero_escolhido = int(input('digite o numero de escolha  :'))


    if numero_escolhido == randor_number:
        print('voce acertou na tentativa {}'.format(tentativas))

    elif numero_escolhido < randor_number:
        print('esta a baixo')
    elif numero_escolhido > randor_number:
        print('esta acima')






