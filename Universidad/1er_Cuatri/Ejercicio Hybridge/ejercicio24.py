'''
/*
Para todos los números naturales menores al 1000000 determina cual es el número palíndromo más grande.
*/
'''


cadena = []

def polindromos_pares(rango):

    poli_pares = []
    for i in range(rango):
        if i % 2 != 0:
            poli_pares.append(str(i)[0:3])
    return poli_pares



def voltear_pares(lista):
    lista_volteada = []
    for i in lista:
        lista_volteada.append(i[::-1])
    return lista_volteada

def transformarnombres(cadena1, cadena2):
    lista_final=[a+b for a, b in zip(cadena1, cadena2)]
    return lista_final

def transform_int(cadena):
    lista_int = [int(x) for x in cadena]
    return lista_int

cadena = polindromos_pares(1000)
cadena_volteada = voltear_pares(cadena)
final = transformarnombres(cadena, cadena_volteada)
valores_int = max(transform_int(final))
print(f'Numero palindromo mas grande menor a 1,000,000 es: {valores_int}')




