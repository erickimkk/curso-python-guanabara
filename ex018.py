import random



randon_num = random.randint(0,100)
while True:
    try:
     numero = int(input('adivinhe o numero de 0 a 100 :'))

     if numero < randon_num:
      print('foi menor do que o numero')
     elif numero > randon_num:
      print('foi maior do que o numero')
     else:
      print('parabens voce acertou!')
      break
    except ValueError:
     print('please insert a valid number !')


