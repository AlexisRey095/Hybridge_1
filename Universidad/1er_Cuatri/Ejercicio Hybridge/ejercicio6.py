'''
/*
Realiza un programa que le pida un número entero a un usuario y le diga si es par o impar.
*/
'''

numero = int(input('Ingresa numero: '))
calculo = numero % 2

if calculo == 1:
    print(f'tu numero {numero}, es un numero impar')
else:
    print(f'tu numero {numero}, es un numero par')