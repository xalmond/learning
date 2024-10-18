# Abrir, leer y cerrar archivos

mi_archivo = open('data/prueba_practica_006_01.txt')
print()
print(mi_archivo)
print()
print(mi_archivo.read())
mi_archivo.close()

mi_archivo = open('data/prueba_practica_006_01.txt')
print()
print(mi_archivo.readline().rstrip())  # Quita fin de línea dque viene del archivo
print(mi_archivo.readline())
print(mi_archivo.readline())
mi_archivo.close()

mi_archivo = open('data/prueba_practica_006_01.txt')
print()
print(mi_archivo.readlines())
print(mi_archivo.readlines())
mi_archivo.close()

# Crear y escribir archivos

mi_archivo = open('data/prueba_practica_006_02.txt', 'w')  # Si no existe, lo crea
mi_archivo.write('Soy el nuevo texto')
mi_archivo.close()

mi_archivo = open('data/prueba_practica_006_02.txt', 'w')  # Si existe, lo borra
mi_archivo.write('Soy el nuevo texto, cuidado que no se ha añadido al anterior')
mi_archivo.write('Soy el más nuevo sin salto de línea')
mi_archivo.write('\nYo si llevo salto de línea')
mi_archivo.close()

mi_archivo = open('data/prueba_practica_006_02.txt', 'a')  # Coloca el cursor al final del fichero
mi_archivo.write('\nSoy el texto añadido al final')  # Cuidado con salto de línea inicial
mi_archivo.close()

# Directorios

import os
print()
print(os.getcwd())
os.chdir('C:\\Users\\jalmen\\Documents\\learning\\python_total\\data')  # Cuidado con barras invertidas
print(os.getcwd())
mi_archivo = open('prueba_practica_006_01.txt')
print(mi_archivo.readlines())
mi_archivo.close()
ruta = 'C:\\Users\\jalmen\\Documents\\learning\\python_total\\data\\prueba_practica_006_01.txt'
print()
print(os.path.dirname(ruta), os.path.basename(ruta), os.path.split(ruta))

os.chdir('C:\\Users\\jalmen\\Documents\\learning\\python_total\\data')  # Cuidado con barras invertidas
os.mkdir('otra_data')
os.rmdir('otra_data')

from pathlib import Path, PureWindowsPath
directorio = Path('/Users/jalmen/Documents/learning/python_total/data')  # No hace falta C: ni barras invertidas
archivo = directorio / 'prueba_practica_006_01.txt'  # Cuidado con esta sintaxis
mi_archivo = open(archivo)
print()
print(mi_archivo.readlines())
mi_archivo.close()

# Módulo pathlib
archivo = Path('C:/Users/jalmen/Documents/learning/python_total/data/prueba_practica_006_01.txt')
print()
print(archivo.read_text())
print()
print(archivo.name, archivo.suffix, archivo.stem)
if archivo.exists():
    print('El archivo existe')
print(PureWindowsPath(archivo))

# Path

base = Path.home()
curso = Path('learning', 'python_total')
ruta = Path(base, 'Documents', curso, Path('data', 'prueba_practica_006_01.txt'))
print()
print(ruta)
print(ruta.parent, ruta.parent.parent)
ruta2 = ruta.with_name('prueba_practica_006_02.tx')
print()
print(ruta2)
print()
for i in Path(base, 'Documents', curso).glob('*.py'):
    print(i)
print()
for i in Path(base, 'Documents', curso).glob('**/*.txt'):
    print(i)
print()
print(ruta.relative_to(base))

# Limpiar la consola

print()
nombre = input('Dime tu nombre: ')
edad = input('Dime tu edad: ')
os.system('cls')
print(f'Tu nombre es {nombre} y tienes {edad} años.')