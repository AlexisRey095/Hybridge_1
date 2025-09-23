'''
Sacando numros primos 

'''

numero = int(input('Ingresa un valor: '))

verificador = [2,3,4,5,6,7,8,9]
num_primos = []
mensaje = ''



def es_primo(valor):  

    contador = valor
    status = False    

    while status == False:

        if valor %2 ==0:
            contador = valor + 1
        else:
            for n in verificador:
                if contador%n == 0:
                    mensaje = 'no aplica 2do nivel'
                    return mensaje

                if  contador%n != 0:
                    mensaje = 'primo'
                    num_primos.append(n)
                    if len(num_primos) == 2:
                        status = True
                        return num_primos[-1], mensaje

print(es_primo(numero))
