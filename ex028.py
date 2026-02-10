#Listas
#Sao mutaveis

pedido = ['lanche','refri','sorvete']
#aqui eu coloco o cokkie na frente
pedido.append('cokkie')
#aqui eu escolho onde eu quero, mas ele nao substui ele reorganiza os da frente para pular um
pedido.insert(0,'cokkie')

#apagar elementos pelo indice
del pedido[0]
pedido.pop(3)

#apagar pelo valor
pedido.remove('refri')

valores = list(range(0,5))
print(valores)