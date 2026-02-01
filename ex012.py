distancia = int(input('digite a distancia da viagem: '))

if distancia <= 200:
    passagem = distancia * 0.5

else:
    passagem = distancia * 0.45

print('o preco da passagem vai ser {}'.format(passagem))
