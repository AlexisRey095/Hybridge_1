'''
Crear un programa en Python que simule una calculadora de descuentos para una tienda en línea. 
El programa debe pedirle al usuario ciertos datos y, basándose en ellos, determinar si aplica un descuento, 
cuánto será y mostrar un mensaje personalizado. La tienda tiene las siguientes reglas para otorgar descuentos:

- Si el usuario es miembro premium y su compra es mayor a $500, recibe un 20% de descuento.
- Si el usuario no es miembro premium pero su compra es mayor a $1000, recibe un 10% de descuento.
- Si el usuario es estudiante y su compra es mayor a $200, recibe un 15% de descuento.
- Si no cumple ninguna de estas condiciones, no recibe descuento.

'''

#Saludo de programa 
print ('--- Programa ckeckPoint 5 ----- ')

#Inputs del usuario
status = input('Eres miembro Premium? (S/N)')
es_estudiante = input('Eres estudiante? (S/N)')
monto = int(input('Monto de tu compra? '))

#Logica 
if status == 'S' and monto > 500:
    total = monto*(1-0.2)
elif status != 'S' and monto > 1000:
    total = monto*(1-0.1)
elif es_estudiante == 'S' and monto > 200:
    total = monto*(1-0.15)
else:
    total = monto #Problema detectado, olvide igualar la variable total en el ELSE

print(total)