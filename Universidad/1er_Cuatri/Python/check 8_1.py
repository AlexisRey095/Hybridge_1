usuarios = [ 
  {"user": "ana", "password": "1234"},
  {"user": "juan", "password": "abcd"},
  {"user": "maria", "password": "pass"},
  {"user": "alexis", "password": "123"}
]

def verificacion_user():
    valor_user = input('Ingresa tu Usuario: ')
    for i, user_data in enumerate(usuarios):
        if user_data['user'] == valor_user:
            return i
    print("Usuario no encontrado")
    return -1

def verificacion_pass(indice):
    if indice == -1:
        return False
    
    valor_pass = input('Ingresa tu password: ') 
    if usuarios[indice]['password'] == valor_pass:
        print(f'Bienvenido/a {usuarios[indice]["user"]}! Acceso concedido.')
        return True
    else:
        print('Password Incorrecto')
        return False

contador = 3

while contador > 0:
    usuario = verificacion_user()
    password = verificacion_pass(usuario)

    if password:
        break
    else:
        contador -= 1
        if contador > 0:
            print(f"Te quedan {contador} intentos")

if contador == 0:
    print('Cuenta bloqueada por exceder el número máximo de intentos')