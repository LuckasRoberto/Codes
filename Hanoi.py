import pygame

def torre_de_hanoi(n, x, y, z):
    if n == 1:
        print('Mova disco %s de %s para %s' %(n, x, y))
        print(x, y, z)
    else:
        torre_de_hanoi(n-1, x, z, y)
        print('Mova disco %s de %s para %s' %(n, x, y))
        print(x, y, z)
        torre_de_hanoi(n-1, z, y, x)

num = int(input('Número de discos:'))
numero = num
a = 'X'
b = 'Y'
c = 'Z'
print(a, b, c)
torre_de_hanoi(numero, a, b, c)
