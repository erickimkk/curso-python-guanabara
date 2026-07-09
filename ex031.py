idade = int(input('digite a dua idade '))

if idade >= 18:
    print('vpce deveria se candidatar em {}'.format( 2026 - (idade - 18)))
elif idade < 18:
    print('ainda faltan {} para voce se alistar ao exercicito, seu alistamento sera em {}'.format((18 - idade ),(2026 + (18 - idade))))