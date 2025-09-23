"""
Programa que simula la pokedex de acuerdo a los pokemones
se vayan atrapando empieza con 3, requisitos:
1. debe agregar nombre del pokemon
2. debe agregar tipo del pokemon 
3. debe agrear numero del pokemon 
4 El usuario puede ver el pokemon si pone el numero con las specs del pokemon
5. en caso de no existir el pokemon o no estar atrapado, debe mosrtar en pantala


"""

print('======== Pokedex Primera Version ======== ')

pokedex = [

    {
        '001':{'nombre':'Pykachu', 'tipo':'electrico'},
        '002':{'nombre':'Charizard', 'tipo':'fuego'},
        '003':{'nombre':'Garadous', 'tipo':'agua'}
    }

]

#empiezo de la logica de la pokedex

add_pokemon = input('Has capturadoro un Pokemon? (s/n) ')
add_pokemon.lower()
review_pokedex = input('Desea revisar tu pokedex? (s/n)')
review_pokedex.lower()
registro = ''


if add_pokemon == 's' and review_pokedex == 'n':

    #Variables de verificacion de ingreso
    add_name = input('Ingresa el nombre del pokemon: ')
    add_num = (input('Ingresa el numero del pokemon: '))
    add_type = input('Ingresa el tipo de pokemon: ')

    #logica para agregar un nuevo dic por input
    pokedex[0][add_num] = {
        'nombre':add_name,
        'tipo':add_type
    }

    registro = 'Pokemon Capturado'
    print(pokedex)

elif add_pokemon == 'n' and review_pokedex == 's':

    #Accediendo a la estructura 
    search_num = input('Nnumero de Pokemon:  ')

    if search_num in pokedex[0]:

        #Obteniendo los datos de la estructuran
        name_pokemon = pokedex[0][search_num]['nombre']
        type_pokemon = pokedex[0][search_num]['tipo']

        print()
        print('Pokemon Buscado: ', search_num)
        print('Nombre del Pokemon: ', name_pokemon)
        print('Tipo de pokemon: ', type_pokemon)
    
        registro = 'Pokedex Actualizado'
        print(registro)
    else:
        registro = 'Ese pokemon no ha sido capturado'
        print(registro)

else:  
    registro = 'Sin Actualizaciones'
    print(registro)
    

