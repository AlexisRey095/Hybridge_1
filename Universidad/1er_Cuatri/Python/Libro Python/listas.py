#*ejercicio para trabajar lo trabajo en la seccion 3 del libro

'''places = ['tlaxcala', 'veracruz', 'guadalajara', 'tequila', 'durango']
print (places)
print (sorted(places, reverse=True))
print (places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print(len(places))'''

#*----- Trabanandon con numeros en listas

print('\n')
for value in range(1,21):
    print(value)

#?-Reviesar for million in range(1,1_000_001):
    #?-revisar print(million)

print('\n')
for impar in range(1,21,2):
    print(impar)

print('\n')
pares = []
for par in range(1,31):
    if par%3 == 0:
        pares.append(par)
print(pares)

print('\n')
cubos = [valor**3 for valor in range(1,11)]
print(cubos)

print('\n')
print(places[1])

# *Trabajando con Datos avanzados en listas ------ 

#Ejercicio 2

usernames = ['alex', 'karen', 'pedro', 'admin', 'antonio']

for username in usernames:
    if username == "admin":
        print('Hola Admin,  Quieres ver el repore de hoy?')
    else:
        print(f'hola {username}, un gusto saludarte')

if usernames:
    for username in usernames:
            if username == 'admin':
                print('Hola Admin ¿deseas el reporte de hoy?')
            else:
                 print(f'Hola {username}, un gusto saludarte!',"\n")
else:
     print('Lista vacia',"\n")


#Ejercicio 3 

current_user = ['ALex', 'karen', 'pedro', 'admin', 'antonio', 'karina', 'Diana', 'practis']
current_user_lower = [item.lower() for item in current_user]

new_users = ['alex', 'juan', 'goliat', 'diana']

for new_user in new_users:
    if new_user in current_user_lower:
        print('Usuario ocupado, definir otro nombre')
    else:
        print('Nombre de usuario disponible')
