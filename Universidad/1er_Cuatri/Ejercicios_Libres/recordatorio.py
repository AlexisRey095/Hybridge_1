#Calculadora con python en 2 sencillos pasos


menu = (input('\n Que operacion necesitas?\n' \
'1. Suma\n' 
'2. Resta\n' \
'3. Multiplicacion\n' \
'4. Division\n'
 ))


def suma (numero1, numero2):
        operacion = numero1 + numero2
        return (operacion)

def resta (numero1, numero2):
        operacion = numero1 - numero2
        return (operacion)

def division (numero1, numero2):
        operacion = numero1 / numero2
        return (operacion)

def multiplicacion (numero1, numero2):
        operacion = numero1 * numero2
        return (operacion)

numero1 = int(input('ingresa numero 1: '))
numero2 = int(input('ingresa numero 2: '))

if menu == '1':
        print(f' Resultado: {suma(numero1, numero2)}')
elif menu == '2':
        print(f' Resultado: {resta(numero1, numero2)}')
elif menu == '3':
       print(f' Resultado: {multiplicacion(numero1, numero2)}')
elif menu == '4':
        print(f' Resultado: {division(numero1, numero2)}')
else:
        print('Opcion no valida')


    
       