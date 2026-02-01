# tuplas
#tuplas sao imutaveis
lanche = ('Hamburguer','Suco','Pizza','Pudim')
for i in range(0,len(lanche)):
    print(lanche[i])

#os dois sao a mesma coisa

for pos,i in enumerate(lanche):
    print(f'vou comer {i} na posicao {pos}')


