contagem  = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
valor = int(input('dogote um valor entre 0 e 20 :'))
if (valor > 20) or (valor < 0):
    print('o numero digitado nao esta ente 0 e 20')
else:
    print(f'voce digitou o numero {contagem[valor]}')