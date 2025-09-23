'''
Implementa un programa que valide un usuario y contraseña usando ciclos for y while.
El usuario tiene un máximo de 3 intentos para ingresar correctamente sus credenciales.
Requisitos
Tienes una lista de diccionarios llamada usuarios.
Cada diccionario contiene dos llaves: "user" y "password".
Utiliza un ciclo while para permitir al usuario un máximo de 3 intentos para iniciar sesión.
Dentro del ciclo while, usa un ciclo for para recorrer la lista y validar el usuario y contraseña.
Si las credenciales son correctas, muestra un mensaje de bienvenida y termina el programa.
Si se agotan los 3 intentos sin éxito, muestra un mensaje indicando que la cuenta está bloqueada.

'''



#Inicio del programa

usuarios = [ 
  {"user": "ana", "password": "1234"},
  {"user": "juan", "password": "abcd"},
  {"user": "maria", "password": "pass"},
  {"user": "alexis", "password": "123"}
]

def verificacion_user():

    valor_user = input('Ingresa tu Usuario: ')
    usuario = False
    index_encontrado = -1
    index = 0
    while  not usuario:  
        for i, user_data in enumerate(usuarios):
            if user_data['user'] == valor_user:
                usuario = True
                index_encontrado = i
                return index_encontrado 

            else:
                usuario = False
                index = index + 1


def verificacion_pass(indice):
    valor_pass = input('Ingresa tu password: ') 
    password = False
    if usuarios[indice]['password'] == valor_pass:
        password = True
        print('Acceso al sistema')
        return password
       
    else:
        print('Password Incorrecto')
        return password 


#ejecucion programa

contador = 3

while contador > 0:

    usuario = verificacion_user()
    password = verificacion_pass(usuario)

    if usuario >= 0:
        if password == True:
            break
        else:
            contador = contador - 1


if contador == 0 :
    print('cuenta bloqueada')






