
#! ejercicio1, pedir nombre de carro 

'''name_car = input('\nintroduce nombre del auto buscado: ')

print(f'Buscando carro tipo: {name_car}')'''

#! Ejercicio2 _ Restaurant book

'''ppl = int(input('\n How many pple will come to have dinner tonigh?: '))

if ppl >=8:
    print('Srry, We dont have enough tables')
else:
    print('You are welcome')'''

#! Ejercicio3 _ Numeros pares o primos

'''number = int(input('\nIntroduce a number: '))
if number%2==0:
    print('the number is par')
else:
    print('the number is primo')'''

#! Exercise5_ PizzaTopping

prompt = '\nPlease add the topping that you want in your pizza: '
prompt += '\nWrite "quite" to exit\n '
topping_list = []
while True:
    topping = input(prompt).lower() #todo>>>> Agregar el metodo .lower despues del prompt
    if topping != 'quite':
        topping_list.append(topping)
    else:
        break

print(f'\nYour Pizza will have: {topping_list}')