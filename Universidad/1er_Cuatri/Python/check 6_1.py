print(' =======  Bienvenido al programa de registro de Turismo ======== ')

#Registro de datos
destinos = [
    {
        'destino':'California',
        'actividades':['jugar futbol', 'patinar'],
        'costo':10000,
    },
    {
        "destino":'New York',
        'actividades':['mirador', 'tomar cafè'],
        'costo':10000,
    }
]
   

valor_destino1 = input('Agrega una actividad al destino 1: ')
change_cost_destino2 = int(input('Modifica el costo del segundo viaje: '))

#agregando valores
destinos[0]['actividades'].append(valor_destino1)  # Agregar actividad al primer viaje
destinos[1]['costo'] = change_cost_destino2  # Cambiar costo del segundo viaje

print(destinos)