'''
Ejercicio que cuente por serpado los numeros que pasas por consola

'''




def suma_numeros():

 
    lista_numeros_str = []

    while True:

        numero = input('Ingresa un numero mayor a 2 digitos: ')

        if  len(numero) >=2:  
            for i in numero:
                lista_numeros_str.append((i))

            lista_numeros_int = list(map(int, lista_numeros_str))
            suma = 0
            for j in lista_numeros_int:
                suma = j + suma
            True
            return suma          
        else:
            print('Numero no aceptable, intenta de nuevo')
            False
            


print(f'La sumatoria de cada unos de los digitos de tu cantidad es: {suma_numeros()}')

