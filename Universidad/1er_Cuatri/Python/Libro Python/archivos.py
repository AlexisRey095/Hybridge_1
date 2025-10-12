
#! Trabajando con archivos en python

'''from pathlib import Path

path = Path('/Users/aviantowebstudio/downloads/alexis/universidad/1er_cuatri/hybridge_1/universidad/1er_cuatri/python/Libro Python/texto.txt')
contents = path.read_text()

lines = contents.splitlines()
text_line = ''
for line in lines:
    text_line += line.lstrip() #! >>> la str vacia se va llenando con este loop

looking_word = input('Writte the word that you lokking for: ')

if looking_word in text_line:
    print('Se encuentra en el texto')
else:
    print('No se encuentra en el texto')
'''

#! Escribiendo en el archivo 

from pathlib import Path

contents = 'I love programming\n'
contents += 'I love my new skills\n'
contents += 'I want to change the world with it'

path = Path('/Users/aviantowebstudio/downloads/alexis/universidad/1er_cuatri/hybridge_1/universidad/1er_cuatri/python/Libro Python/programming.txt')

path.write_text(contents)