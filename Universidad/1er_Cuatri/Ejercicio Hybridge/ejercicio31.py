'''
numero amigables: Por ejemplo: 220 tiene como suma de divisores: 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284 
Y 284 tiene como suma de divisores: 1 + 2 + 4 + 71 + 142 = 220

Encuentra todos los pares de números menores a 1000 que sean mutuamente amigables.

'''

lista_amigables = []

#Algoritmo para saber si es un valor amigable
def valor_amigable (valor):
    pares1 = []
    suma_dividendos1 = 0


    for i in range(1, valor+1):
        if valor%i ==0 and valor/i !=1: #Comprobamos que no se incluya el numero Valor
            pares1.append(i)
            suma_dividendos1 += i

    pares2 = []
    suma_amigables = 0

    for j in range (1, suma_dividendos1+1):
        if suma_dividendos1%j ==0 and suma_dividendos1/j !=1:
            pares2.append(j)
            suma_amigables += j
    
    if valor == suma_amigables:
        return True
        


for i in range(1,1000):
    if valor_amigable(i) == True:
        lista_amigables.append(i)

print(f'valor amigables menores a 1000: {lista_amigables } ')