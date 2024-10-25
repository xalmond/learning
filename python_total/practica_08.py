# Módulos y paquetes

from practica_08_package import sumar_y_restar
from practica_08_package.practica_08_subpackage import multiplicar_y_dividir

print(sumar_y_restar.sumar(2, 7), sumar_y_restar.restar(2, 7))
print(multiplicar_y_dividir.multiplicar(2, 7), multiplicar_y_dividir.dividir(2, 7))

# Manejo de errores

def divide():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    print(n1 / n2)
    print('Gracias por dividir')

try:
    # divide()
    print()
except ValueError:
    print('No has introducido un número')
except:
    print('Algo no ha funcionado')
else:
    print('Todo funcionó perfectamente')
finally:
    print('Se acabó lo de dividir')


# Decoradores

def cambiar_palabra(tipo):
    def mayuscula(texto):
        return texto.upper()
    def minuscula(texto):
        return texto.lower()
    if tipo == 'may':
        return mayuscula  # Se pueden devolver funciones
    else:
        return minuscula

print()
operacion = cambiar_palabra('may')
print(operacion('Javier'))  # Las funciones son objetos en sí mismas
print(cambiar_palabra('may')('Javier'))  # Las funciones son objetos en sí mismas


def decorar_con_simpatia(funcion):

    def nueva_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return nueva_funcion

@decorar_con_simpatia
def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

print()
mayusculas('Javier Almendro')  # Siempre con decorador
minusculas('Javier Almendro SIN DECORAR')  # Sin decorador
minuscula_decorada = decorar_con_simpatia(minusculas)
minuscula_decorada('Javier Almendro DECORADA')  # Decorada
print(minuscula_decorada)
decorar_con_simpatia(minusculas)('Javier Almendro')  # Otra forma de decorar una vez


# Funcionas generadoras o generadores

def mi_funcion():
    return [i * 10 for i in range(1, 5)]

def mi_generador():
    for i in range(1, 5):
        yield i * 10

print()
print(mi_funcion())
print(mi_generador())
g = mi_generador()  # Importante inicializar una variable con el resultado de la función generadora
print(next(g))
print('Ahora genero el siguiente valor: ', next(g)) # Cuidad, da error si sobrepaso el límite

def otro_generador():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x

g = otro_generador()
print()
print(next(g))
print(next(g))
print('puedo intercalar código que recuerda el último next')
print(next(g))