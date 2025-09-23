'''
/*
Pide al usuario su peso (kg) y su estatura (m). Calcula el IMC
*/
'''

peso = float(input('Ingresa tu peso en "KG": '))
estatura = float(input('Ingresa tu estatura en "m": '))

calculo = (peso / (estatura**2))

print(f'Tu indice de masa corporal es: {calculo}')