'''
numero faactorial de un numero y sumar sus digitos
'''
import math
valor = 100
resultado = math.factorial(valor)
lista_factorial_int = [resultado]
lista_factorial_str = list(map(str, lista_factorial_int))
lista_formateada_str = []


for numero_str in lista_factorial_str:
    for digito in numero_str:
        lista_formateada_str.append(digito)

lista_formateada_int = list(map(int, lista_formateada_str))

suma = 0
for i in lista_formateada_int:
    suma = suma + i

print(suma)
