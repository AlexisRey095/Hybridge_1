'''
/*
Dada la lista [5, 1, 9, 3, 7, 8, 4, 2, 6, 10, 3, 5, 2], encuentra el producto más alto de tres números consecutivos.
*/


lista = [1, 2, 3, 4, 5]
max_index = len(lista)-1
contador1 = 1
contador2 = 2
nueva_lista = []
lista_final = []

while  contador2 <= max_index:
    for i in lista:
        i = lista[contador1]*lista[contador2] * i
        nueva_lista.append(i) 
        contador1 +=1
        contador2 +=1
        
        if contador2 or contador1 == max_index:
            break

print(nueva_lista)''' 

lista = [5, 1, 9, 3, 7, 8, 4, 2, 6, 10, 3, 5, 2]
mayor_producto = 0

for i in range(len(lista) - 2):
    producto = lista[i] * lista[i + 1] * lista[i + 2]
    if producto > mayor_producto: #esto empieza en 0 y tomara ese valor comparativo por cada bucle
        mayor_producto = producto

print("El mayor producto de 3 elementos consecutivos es:", mayor_producto)