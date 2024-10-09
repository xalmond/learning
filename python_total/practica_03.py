# Método index()

mi_texto = 'Esta es una prueba'
print(mi_texto.index('n'), mi_texto.index('prueba'))
print(mi_texto.index('a'), mi_texto.index('a', 5), mi_texto.rindex('a'))

# Slicing

text = 'ABCDEFGHIJKLM'
print(text[:3], text[3:], text[3:10], text[3:10:2], text[::2], text[::-1])

# Métodos de string
texto = 'Este es el texto de Javier'
print(texto.upper(), texto[2:10].upper(), texto.lower())
print(texto.split(), '\n', texto.split('e'), '\n', texto.lower().split('e'))
print('_'.join(texto.split()))
print(texto.find('Javier'), texto.find('Xavier'))
print(texto.replace('Javier', 'Jalmen'), texto.replace('e', 'E'))

# Propiedades de los strings
print('Kari' + 'na', 'Kari' * 2)
print('''Hola,
que tal?''')
texto = 'Este es el texto de Javier'
print('Javier' in texto, 'Xabier' not in texto)
print(len(texto))

# Listas

lista = ['a', 'c', 'b']
print(lista, lista[0:2], lista[::-1], len(lista), lista+lista, '\n', lista*3)
lista[2] = 'beta' # No es inmutable
lista.append('d')
print(lista)
lista.pop()
print(lista)
eliminado = lista.pop(0)
print(lista, eliminado)
vacio = lista.sort()
print(lista, vacio, type(vacio))  # IMP!!!!
lista.reverse()
print(lista)

# Diccionarios

cliente = {'nombre': 'Javier', 'apellido': 'Almendro', 'peso': 90, 'altura': 1.86}
print(cliente['apellido'])
print(cliente.keys(), cliente.values())
print(cliente.items())  # El resultado son tuplas
dic = {'c1': 54, 'c2': [1, 2, 3], 'c3': {'s1': 100, 's2': 200}}
print(dic['c2'], dic['c2'][1], dic['c3']['s2'])
dic =  {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic['c2'][1].upper())
dic['c3'] = ['g', 'h']
dic['c2'] = ['f', 'e', 'd']
print(dic)

# Tuplas

tupla = (1, 2, (35, 36), 2)
print(tupla[2][1], tupla.count(2), tupla.index(2), tupla.index(2,2))
lista = list(tupla) # Casting
lista[2] = 2.5
print(lista)
a, b, c, d = tupla
print(a, b, c, d)

# Sets

mi_set = {1, 2, 3, 4, 5, 1} # Descarte el segundo 1
print(mi_set, type(mi_set))
otro_set = {1, 2, 3, (1, 2), 'Javier'}
print(otro_set, 'Javier' in otro_set, len(otro_set))
print(mi_set.union(otro_set))
otro_set.add('Almendro')
print(otro_set)
otro_set.remove((1, 2))
print(otro_set)

# Booleans

valor = 5 > 7
control = 3 in mi_set
print(valor, control)




























