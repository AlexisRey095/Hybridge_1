'''
/*
Pide un número al usuario y dile si es positivo, negativo o cero.
*/
'''

numero = int(input('ingresa un numero: '))

if numero <= -1:
    print(f'tu numero {numero} es, negativo')
elif numero >= 1:
    print(f'tu numero {numero} es, positivo')
else:
    print(f'tu numero es Cero')