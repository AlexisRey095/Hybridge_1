'''
ejercicio que muestra una calculadora mediante funciones
'''

fin = False
resultado = 0

print ('\n ----- Calculadora ------\n')
print( 'Menu:' 
'\n1. Sumar' \
'\n2. Restar' 
'\n3. Multiplicar' \
'\n4. Dividor' \
'\n5. Salir'
      )

def sumar(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

def restar(valor1, valor2):
    resultado = valor1-valor2
    return resultado

def multiplicar(valor1, valor2):
    resultado = valor1 * valor2
    return print(resultado)

def dividir(valor1, valor2):
    resultado = valor1/valor2
    return print(resultado)

def salir():
    return True



while fin == False:
    select = int(input('Introduce el numero de funcion: '))
    valor1 = int(input('Introduce valor 1 de la operacion: '))
    valor2 = int(input('Introduce valor 2 de la operacion; '))
    if select == 1:
            valor = sumar(valor1, valor2)
            print(valor)
        
    elif select == 2:
            valor = restar(valor1, valor2)
            print(valor)
        
    else:
            print('Saliendo...')
            break
            