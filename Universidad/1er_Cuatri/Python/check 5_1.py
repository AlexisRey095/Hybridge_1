#Inputs del usuario
status = input('Eres miembro Premium? (S/N)')
es_estudiante = input('Eres estudiante? (S/N)')
monto = int(input('Monto de tu compra? '))

#Variables logica
descuento = None
mensaje = ''

#Logica 
if status == 'S' and monto > 500:
    descuento = 0.2
elif status != 'S' and monto > 1000:
    descuento = 0.1
elif es_estudiante == 'S' and monto > 200:
    descuento = 0.15
else:
    descuento = 0

total = ('El monto total a pagar es: $', monto*(1-descuento), 'MXN con un descuento total del: ', descuento*100, ' %')

print(total)