# Módulo collections

import collections
import os

serie = collections.Counter([1,1,1,1,2,3,3,3,4,4])
print()
print(type(serie))
print(serie)
print(serie.most_common(1), serie.most_common(2))

mi_dicc = collections.defaultdict(lambda: 'nada')
print()
print(mi_dicc)
mi_dicc['uno'] = 'azul'
print(mi_dicc)
print(mi_dicc.items())
print(mi_dicc['dos'])  # Simplemente con intentar instanciar se instancia esa clave - valor
print(mi_dicc.items())

Persona = collections.namedtuple('Persona', ['nombre', 'altura', 'peso'])
javier = Persona('Javier', 1.86, 90)
print()
print(f'La altura de {javier.nombre} es {javier.altura} = {javier[1]}')

# Módulos os y shutil

ruta = 'C:\\Users\\jalmen\\Documents\\learning\\python_total\\data'
print()
print(os.walk(ruta))
for carpeta, subcarpeta, file in os.walk(ruta):
    print(f'En la carpeta {carpeta}, tiene las subcarpetas {subcarpeta} y tiene los ficheros {file}')

# Módulo datetime

import datetime

mi_hora = datetime.time(17, 35, 30)
print()
print(mi_hora, mi_hora.hour, mi_hora.minute, mi_hora.second)
mi_dia = datetime.date(2024, 1, 4)
print()
print(mi_dia, mi_dia.year, mi_dia.month, mi_dia.day)
mi_fechahora = datetime.datetime(2024, 1,4, 15, 0)
print()
print(mi_fechahora)
mi_fechahora = mi_fechahora.replace(minute=30)  # Puedo reemplazar cualquier parte del objeto datetime
print(mi_fechahora)
print()
print(datetime.date.today(), datetime.datetime.today())

comienzo = datetime.datetime(1984, 10, 2)
final = datetime.datetime(1994, 2, 21)
print()
print(f'Necesité {(final - comienzo).days} días para acabar la carrera')

# Medir tiempo

import time

def prueba_for(longitud):
    lista = []
    for i in range(longitud + 1):
        lista.append(i)
    return lista
def prueba_while(longitud):
    lista = []
    i = 0
    while i <= longitud:
        lista.append(i)
        i += 1
    return lista

print('\n', prueba_for(20), '\n', prueba_while(20))
print()
inicio = time.time()
prueba_for(1000000)
final = time.time()
print(final - inicio)
inicio = time.time()
prueba_while(1000000)
final = time.time()
print(final - inicio)

import timeit

declaracion = 'prueba_for(10)'
mi_setup = '''
def prueba_for(longitud):
    lista = []
    i = 0
    while i <= longitud:
        lista.append(i)
        i += 1
    return lista
'''
duracion = timeit.timeit(declaracion, mi_setup, number=100000)
print()
print(duracion)

declaracion = 'prueba_while(10)'
mi_setup = '''
def prueba_while(longitud):
    lista = []
    for i in range(longitud + 1):
        lista.append(i)
    return lista
'''
duracion = timeit.timeit(declaracion, mi_setup, number=100000)
print(duracion)

# Módulo math

import math

print()
print(math.floor(12.6), math.ceil(12.4))
print(math.log10(25), math.sqrt(math.pi))
print(math.factorial(7))

# Módulo re - Expresiones regulares

import re

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas del día al servicio de ayuda online'
print()
print('ayuda' in texto)
print(re.search('nada', texto))
print(re.search('ayuda', texto),
      re.search('ayuda', texto).span(),
      re.search('ayuda', texto).start())
print(re.findall('ayuda', texto))
for i in re.finditer('ayuda', texto):
    print(i.span())
print()
print(re.search(r'\(\d\d\d\)-\d\d\d-\d\d\d\d', texto).span(),
      re.search(r'\(\d\d\d\)-\d\d\d-\d\d\d\d', texto).group())  # group empieza en 1
print(re.search(r'\(\d{3}\)-\d{3}-\d{4}', texto).group())
print('\n', re.search(re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4})'), texto).group(1), # Compilo en grupo de subpatrones
      '\n', re.search(re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4})'), texto).group(2))
print(re.search(r'ayuda|AYUDA', texto))
print(re.search(r'.vicio', texto), re.search(r'.{3}vicio', texto))
print()
print(re.findall(r'[^\s]', texto))
print(re.findall(r'[^\s]+', texto))


print()
# clave = input('Clave: ')
# print(re.search(r'^\D{1}\w{7}', clave))  # No puede empezar por dígito y debe tener 8 caracteres

def verificar_email(email):
    if re.search(r'\w+@\w+\.com*\w', email):
        print('Ok')
    else:
        print('La dirección de email es incorrecta')
verificar_email('usuario@hostcom')

# Comprimir / Descomprimir archivos

import zipfile
import os

os.chdir('data/proyecto_09')

mi_zip = zipfile.ZipFile('mi_texto.zip', 'w')
mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')
mi_zip.close()
os.remove('mi_texto_A.txt')
os.remove('mi_texto_B.txt')
print()
print(mi_zip)

mi_zip = zipfile.ZipFile('mi_texto.zip', 'r')
mi_zip.extractall()
mi_zip.close()
print()
print(mi_zip)
os.remove('mi_texto.zip')

os.chdir('../..')

import shutil

os.mkdir('tmp')
os.chdir('tmp')

shutil.make_archive('data_compressed', 'zip', '../data')
shutil.unpack_archive('data_compressed.zip', 'data', 'zip')

os.chdir('..')
shutil.rmtree('tmp')

# Instrucciones del proyecto_09

os.chdir('data/proyecto_09')
shutil.unpack_archive('Proyecto+Dia+9.zip', '.', 'zip')
instrucciones = open('Instrucciones.txt')
for i in instrucciones.readlines():
    print(i.rstrip())
instrucciones.close()




