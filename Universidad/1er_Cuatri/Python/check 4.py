# Crea un programa que convierta una temperatura de grados Celsius a Fahrenheit y determine 
# si es un día caluroso. Un día se considera caluroso si la temperatura en Fahrenheit 
# es mayor o igual a 86°F. 
# 1) Pide al usuario que ingrese una temperatura en grados
#  Celsius usando input. 
# 2) Convierte la temperatura a Fahrenheit usando operaciones aritméticas. 
# 3) Usa un operador de comparación para determinar si es un día caluroso (True o False). 
# 4) Muestra la temperatura en Fahrenheit y si es un día caluroso o no.]
#F = (C * 9/5) + 32

temp = int(input('Ingrese la temperatura en ºC: '))
conversion = (temp*(9/5)) + 32
resultado = conversion >= 86
print('Es un dia caluroso?: ', resultado)

