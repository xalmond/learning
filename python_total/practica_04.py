# Operadores de comparación

print(100.0 == 100, '100' == 100)

# Operaciones lógicas

print(('a' == 'a') and ('b' == 'B'), ('a' == 'a') or ('b' == 'B'))
print(not ('a' == 'a'), not ('a' != 'a'))

# Control de flujo

edad = 16
calificacion = 9
if edad < 18:
    print ('Eres menor de edad')
    if calificacion >= 7:
        print('Tu nota es: Notable')
    elif calificacion >= 5:
        print('Tu nota es: Aprobado')
    else:
        print('Tu nota es: Suspenso')
else:
    print('Eres mayor de edad')

# Loop for

lista = ['luis', 'javier', 'laura', 'francisco']
for i in lista:
    if i.startswith('l'):
        print(f'El nombre {lista.index(i) + 1}º que es {i}, empieza por l')
    else:
        print(f'El nombre {lista.index(i) + 1}º que es {i}, no empieza por l')

for i in 'hola':
    print(i.upper())

for a, b in [[1, 2], [3, 4], [5, 7]]:
    print(f'{a} + {b} = {a + b}')

cliente = {'nombre': 'Javier', 'apellido': 'Almendro', 'peso': 90, 'altura': 1.86}
print()
for i in cliente:
    print(f'{i}: {cliente[i]}')
print()
for i in cliente.items():
    print(f'{i[0]}: {i[1]}')
print()
for i,j in cliente.items():
    print(f'{i}: {j}')

for i in 'Javierín':
    if i == 'r':
        continue
    elif i == 'e':
        break
    print(i)

# Loop while

monedas = 5
print()
while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else:
    print ('No me queda ninguna moneda')

# Rangos

for i in range(5):
    print(i)
print(type(range(5)))
lista = list(range(2, 9, 2))
for i in lista:
    print(i)

# Rangos

print()
lista = ['a', 'b', 'c']
for i in enumerate(lista):
    print(i)
print()
for i, v in enumerate(lista):
    print(i, v)
print()
for i, v in enumerate(range(10, 16)):
    print(i, v)

# zip

nombres = ['Javier', 'Marta', 'Arturo', 'Manolo']
edades = [57, 56, 53]
ciudades = ['Madrid', 'Manresa', 'Rozas']
print()
for x, y, z in zip(nombres, edades, ciudades):
    print(f'{x} tiene {y} años y vive en {z}')

# min y max

print()
print(min('Javier'))
print(min(['Javier', 'Marta', 'Arturo']))
print(min(cliente))

# Aleatorios

import random
print(random.randint(1,50), random.uniform(1, 50), random.random())
print(random.choice(nombres))
random.shuffle(nombres)
print(nombres)

# Compresión de Listas

lista = [random.randint(1,10) for i in range(1000)]
print(max(lista), min(lista))
print([c for c in 'python' if c != 'o'])
print([c if c != 'o' else '0' for c in 'python'])

pies = [10, 20, 30, 40, 50]
metros = [round(x / 3.281, 2) for x in pies]
print()
print(metros)

# match (from 3.10)

serie = 'N-01'
print()
match serie:
    case 'N-01':
        print('Samsung')
    case 'N-01':
        print('Samsung')
    case 'N-01':
        print('Samsung')
    case _:
        print('No existe ese producto')



