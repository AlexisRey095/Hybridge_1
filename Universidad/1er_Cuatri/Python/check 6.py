
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

#Registro de datos
destinos = [
    {
        'destino1':'California',
        'actividades1':['jugar futbol', 'patinar'],
        'costo1':10000,
    },
    {
        "destino2":'New York',
        'actividades2':['mirador', 'tomar cafè'],
        'costo2':10000,
    }
]
   

valor_destino1 = input('Agrega una actividad al destino 1: ')
change_cost_destino2 = int(input('Modifica el costo del segundo viaje: '))

#agregando valores
objetivo_lista = destinos[0]  # --> Primero se debe ingresar al diccionario selecionado
updated_list = objetivo_lista['actividades1'] # --> Entrar a la llave que tiene la lista a modificar
updated_list.append(valor_destino1) # ---> Agregar la cadena a la lista

objetivo_lista2 = destinos[1] 
updated_list2 = objetivo_lista2['costo2']
objetivo_lista2['costo2'] = change_cost_destino2 # ---> Cambia el valor de la llave

print(destinos)


