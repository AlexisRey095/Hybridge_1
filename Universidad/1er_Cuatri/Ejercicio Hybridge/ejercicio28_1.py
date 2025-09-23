
numero = int(input('Ingresa un valor: '))

verificador = [2,3,4,5,6,7,8,9]
num_primos = []
mensaje = ''



def es_primo(valor):  

    contador = valor
    status = False    

    while status == False:

        if contador %2 ==0: #Busca que no sea un valor entero
           status = False
           contador = contador + 1
        elif contador %2 != 0:
            for n in verificador:
                if contador%n == 0: #Busca que no se pueda dividor una segunda vez por un numero
                    mensaje = 'no aplica 2do nivel'
                elif contador%n != 0:
                    mensaje = 'primo'
                    num_primos.append(n)
                    contador = contador + 1
        else:
           mensaje = 'no es un numero'

        if len(num_primos) == 2:
            status = True
            return num_primos[-1], mensaje

print(es_primo(numero))



