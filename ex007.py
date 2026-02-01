import math
an = float(input('digite um angulo que voce quer : '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('o seno desse angulo e {:.2f} '.format(seno))
print('o cosseno desse angulo e {:.2f}'.format(cos))
print('a tangente desse angulo e {:.2f}'.format(tan))