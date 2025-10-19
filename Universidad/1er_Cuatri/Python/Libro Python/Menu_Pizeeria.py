
#programar un menu de comida sin GIU

print('---'*10)
print('\n')
print(''*5, 'PIZZERIA ALEX')
print('\n')
print('---'*10)

#! Funciones 
def menu ():
    print('Menu')
    print('Opciones:\n',
    '1. Pizzas Disponibles.\n',
    '2. Empezar tu pizza.\n',
    '3. Información Tiendas.\n',
    '4. Salir')

def precio (pizza, extra_ingredientes=0):
    costo_pizza = pizza 
    extra_opciones = extra_ingredientes
    total = costo_pizza + extra_opciones
    return total

#! Contenedores

available_pizzas = {
    'hawuaiana':300, 
    'pastor':250, 
    'peperoni':150
    }

ingredientes = {
    'hawuaiana':['queso', 'piña', 'cereza'],
    'pastor':['carne_pastor', 'queso'],
    'peperoni':['queso', 'peperoni'] 
    }

extra_options = {
    'jamon':20,
    'pavo':34,
    'extra_cheese':7,
    'extra_peperoni':15,
    'carne':22
}

option_list = []
contador = 1

#! Logica
menu()
selection_menu = input('Select one option: ')

flag = True

while flag:

    if selection_menu =='1':
        for n in available_pizzas.keys():
            print (f'Pizza {n} is available')
    select_pizza = input('\nwhat would you like order?: ')
    select_pizza = select_pizza.lower()
    if select_pizza in available_pizzas:
        print('\nYour choice content:\n ')
        for ingredient in ingredientes[select_pizza]:
            print(ingredient)
        extra_option = input('\nWould you like to add extra ingredientes?: (y/n)')
        extra_option = extra_option.lower()
        if extra_option == 'y':
            print('\n The extra ingrendientes are: ')
            for option in extra_options.keys():
                print(f'\n{contador}. {option} ,extra ingrediente available')
                contador += 1
            extra_choice = input('\nwould you like to add more ingredientes?: (y/n)\n')
            extra_choice = extra_choice.lower()
            if extra_choice == 'y':
                while flag:
                    extra = input('\nwhat would you like add?: ')
                    extra = extra.lower()
                    if extra in extra_options:
                        option_list.append(extra)
                    else:
                        print('\n Sorry, we dont have this ingredient')
                    salir = input('\nhave you finished?: (y/n)')
                    if salir == 'y':
                        break
            valor = 0
            for n in option_list:
                if n in extra_options:
                    valor += extra_options[n]
            costo = int(available_pizzas[select_pizza])
            print(f'\nThe total cost is ${precio(costo,valor)} MXN')
            flag = False
    if extra_option == 'n':
        costo = int(available_pizzas[select_pizza])
        print(f'\nThe total cost is ${precio(costo)} MXN')
        flag = False
    
    

