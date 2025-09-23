"""
Crea un programa en Python que organice un registro de viajes usando estructuras de datos complejas. El programa debe:
Usar una lista de 2 diccionarios, cada uno representando un viaje.
Cada diccionario debe incluir:
Clave "destino" (string).
Clave "actividades" (lista de 2 strings con actividades planeadas).
Clave "costo" (número entero).
Pedir al usuario con input():
Una nueva actividad para el primer viaje.
Un nuevo costo para el segundo viaje.
Actualizar el primer viaje agregando la actividad a su lista y reemplazar el costo del segundo viaje.
Mostrar con print() la lista completa actualizada.
"""

print(' =======  Bienvenido al programa de registro de Turismo ======== ')


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

#Pedir al usuario las modificaciones 

add_activity = input('Registra una nueva actividad: ')
change_price = int(input('Cambia el precio de la segunda opcion: '))

#accediendo a los valores 
destinos[0]['actividades'].append(add_activity)
destinos[1]['costo'] = change_price

print(destinos)