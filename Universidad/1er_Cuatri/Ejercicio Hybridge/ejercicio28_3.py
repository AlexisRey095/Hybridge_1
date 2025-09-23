'''
Itentando aplicar logica para encontrar numeros primos
'''

numero = int(input('Ingresa un valor: '))

def es_primo(valor):
    #Evaluar que el numero no sea menor a 2
    if valor < 2:
        return False
    #evalua solo hasta la razis del numero y aumenta 1
    for i in range(2, int(valor**0.5) + 1): #el +1 es para que pyrhon itere el ultimo numero tambien
        if valor % i == 0:
            return False
    return True

def siguiente_primo(valor):
    candidato = valor +1 #evalua el sigueinte numero al proporcionado

    while True:
        if es_primo(candidato):
            return candidato
        candidato += 1

resultado = siguiente_primo(numero)
print(f'el siguiente numer primo es: {resultado}')