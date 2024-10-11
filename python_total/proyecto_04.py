# Adivina un número
import random

nombre = input('¿Cuál es tu nombre?: ')
print(f'Hola {nombre}, Tienes 8 intentos para adivinar un número entre 1 y 100.')

intentos = 0
numero = random.randint(1, 100)

while intentos <= 8:
    intentos += 1
    numero_elegido = int(input('Teclea un número: '))
    if numero_elegido not in range(1, 101):
        print('El número elegido no es correcto, por favor, teclea uno que esté entre 1 y 100')
    elif numero_elegido < numero:
        print('El número elegido es menor que le número a adivinar')
    elif numero_elegido > numero:
        print('El número elegido es mayor que le número a adivinar')
    else:
        print(f'Enhorabuena {nombre}. Has acertado el número en {intentos} intentos')
        break
else:
    print(f'Lo siento {nombre}. No has acertado el número {numero} en 8 intentos.')

