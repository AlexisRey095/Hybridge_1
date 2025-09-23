'''
/*
Cuenta cuántos divisores enteros tiene el número 647824 (excluyendo él mismo).
*/

'''

valores_divisibles = []
valor = 647824

for i in range(1,int(valor**0.5)+1):
    if valor % i == 0:
        valores_divisibles.append(i)
    if i != valor//i:
        valores_divisibles.append(valor//i)

if valor in valores_divisibles:
    valores_divisibles.remove(valor)

print(f'la cantidad de valores enteros divisibles es: {len(valores_divisibles)}')

