'''
/*
Encuentra el valor máximo la lista de números [42, 7, 89, 23, 56, 12, 68, 94, 31, 5, 77, 39, 60, 17, 85] sin usar max().
*/
'''

lista = [42, 7, 89, 23, 56, 12, 68, 94, 31, 5, 77, 39, 60, 17, 85]
lista.sort(reverse=True)
print(lista[0])