nome = input('digite seu nome ')

print("seu nome em letras maiusculas e {}".format(nome.upper()))
print('seu nome em letras minusculas e {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('o seu primeiro nome e {} e ele tem {} letra'.format(nome.split()[0], len(nome.split()[0])))
