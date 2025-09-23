
'''
Crea un programa en Python que calcule y organice los gastos de un viaje usando al menos tres funciones. El programa debe:
- Definir y usar estas funciones:
- calcular_transporte(distancia): Recibe la distancia en kilómetros (número), calcula el costo de transporte (distancia * 5 pesos por km), y devuelve el costo.
- calcular_comida(dias, presupuesto_diario=50): Recibe los días del viaje (número) y un presupuesto diario opcional (en pesos), calcula el costo total de comida (días * presupuesto_diario), y devuelve el costo.
- mostrar_resumen(destino, costo_transporte, costo_comida): Recibe el destino (string) y los costos calculados, calcula el costo total (transporte + comida), y devuelve un mensaje con el resumen.
_Pedir al usuario con input():
- El destino del viaje (string).
- La distancia en kilómetros (número).
- Los días del viaje (número).
- Usar las funciones para calcular los costos y mostrar el resumen.
- Mostrar el mensaje final con print().
'''

print ('----- Programa De viajes ------')

#definiendo variables para las funciones

destino = str(input('Cual es su destino?: '))
distancia = int(input('Ingresa la cantidad de km recorridos: '))
dias = int(input('Ingresa la cantidad de dias que dura el viaje: '))
presupuesto_diario = int(input('Ingresa tu presupuesto diario: '))


#definiendo funciones
def calcular_transporte (distancia):
    costo_transporte = distancia*5
    return costo_transporte

def calcular_comidas (dias, presupuesto_diario=50):
    costo_comida = dias * presupuesto_diario
    return costo_comida 

def mostrar_resumen (destino, costo_transporte, costo_comida):
    costo_total = costo_transporte + costo_comida
    mensaje = 'Resumen del viaje a: ', destino, 'Costos del transporte: ', costo_transporte, 'costo por comida: ', costo_comida, 'cargos totales: ', costo_total
    print(mensaje) 


dato1 = calcular_transporte(distancia)
dato2 = calcular_comidas(dias, presupuesto_diario)
dato3 = mostrar_resumen(destino, dato1, dato2)

