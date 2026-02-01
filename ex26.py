continuar = 's'
numero = soma_total = quantidade = maior = menor = avarage =0
while continuar in 's':
    numero = int(input('Digite um numero: '))
    soma_total += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < maior:
            menor = numero
    continuar = input('Deseja continuar? [S/N]').lower().strip()[0]

avarage = soma_total / quantidade

print(f'o maior numero foi {maior} e o menor foi {menor}')
