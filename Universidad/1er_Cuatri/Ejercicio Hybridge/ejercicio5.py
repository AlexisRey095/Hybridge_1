'''
/*
Realiza un programa que convierta dólares a pesos usando un tipo de cambio fijo (1 USD = 20.5 MXN).
*/

'''

dolares = float(input('Cantidad de dolares a cambiar: '))
logica = dolares*20.5

print(f'La cantidad de pesos por ${dolares} USD son: ${logica}MXN')