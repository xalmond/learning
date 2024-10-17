# Métodos y ayuda python

cliente = {'nombre': 'Javier', 'apellido': 'Almendro', 'peso': 90, 'altura': 1.86}
print(cliente.popitem(), cliente.popitem(), cliente)

cadena = ',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#'
print(cadena.lstrip(',:%_#'), cadena)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, 'naranja')
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
print(marcas_smartphones.isdisjoint(marcas_tv))

# Funciones

def invertir_palabras(palabra):
    '''
        Esta función hace dos cosas:
            - Invierte la palabra
            - La pone en mayúsculas
    '''
    return palabra[::-1].upper()
print()
print(invertir_palabras('Javier'))

def todos_pares(lista):
    for x in lista:
        if x%2 != 0:
            return False
    return True
print()
print(todos_pares([1,2,15,7,2]))

# Interacción entre funciones

from random import shuffle, choice
palitos = ['-', '--', '---', '----']
def mezclar(lista):
    shuffle(lista)
    return lista
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un palito del 1 al 4: ')
    return int(intento)
def chequear_intento(lista, intento):
    if lista[intento -1] == '-':
        print('A lavar los platos')
    else:
        print('Esta vez te has librado')
    print(f'Te ha tocado el palito {lista[intento -1]}')
# chequear_intento(mezclar(palitos), probar_suerte())

def reducir_lista(lista_numeros):
    lista_reducida = list(set(lista_numeros))
    lista_reducida.pop()
    return lista_reducida
def promedio(lista_numeros):
    suma = 0
    for x in lista_numeros:
        suma = suma + x
    return suma / len(lista_numeros)
print()
print(promedio(reducir_lista([1,2,15,7,2])))

# Argumentos indefinidos *args

def suma(*args):
    return sum(args)
print()
print(suma(1,2,15,7,2))

# Argumentos indefinidos **kwargs
def suma(**kwargs):
    print(kwargs, kwargs.items())
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
    return sum(kwargs.values())
print()
print(suma(x=1, y=2, z=3))

def prueba_todo(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')
    print(f'La suma de los args es {sum(args)}')
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
print()
prueba_todo(1,2,3, 4, 5, 6, 7, a=10, b=12, c=14)
print()
args = [3, 4, 5, 6, 7]
kwargs = {'a': 10, 'b': 12, 'c': 14}
prueba_todo(1,2,*args, **kwargs)

def devolver_distintos(x, y, z):
    lista = [x, y, z]
    suma = sum(lista)
    if suma > 15:
        return max([x, y, z])
    elif suma < 10:
        return min([x, y, z])
    else:
        lista.sort()
        return lista[1]
print()
print(devolver_distintos(4,2,3))

def abcde(palabra):
    lista = list(set(list(palabra)))
    lista.sort()
    return lista
print()
print(abcde('entretenido'))

def doble_cero(*args):
    for i, x in enumerate(args[:-1]):
        if x == 0 and args[i+1] == 0:
            return True
    return False
print()
print(doble_cero(1,2,3,4,5,6,0,0))

def es_primo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True
def contar_primos(numero):
    if numero <= 1:
        return 0
    else:
        primos = 0
        for i in range(2, numero+1):
            if es_primo(i):
                primos += 1
        return primos
print()
print(contar_primos(17))







