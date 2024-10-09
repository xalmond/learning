# Variables

nombre = 'Javier'
print('Tu nombre es ' + nombre)

# integers and floats

numero = 5
print(type(numero), numero, numero + numero)
numero = 1.2
print(type(numero), numero, numero + numero)
numero = 5
print(type(numero), type(numero*1.2), type(numero*1.0))

# type of input

edad = input('Dime tu edad: ')
print(type(edad), edad + edad)

num1 = 7.5
num2 = 2.5
print(type(num1+num2))

# Conversiones

numero_decimal = 5.7
numero_entero = int(numero)
print(numero_entero, type(numero_entero))

nueva_edad = int(edad) + 1
print('El año que viene tendrás ' + str(nueva_edad))

# Formatear cadenas con format (old)

x = 10
y = 5
print('Mis números son {} y {}'.format(x, y))
print('La suma de {} y {} es {}'.format(x, y, x+y))

# Formatear cadenas con cadenas literales (new from python 3.6)

color = 'blanco'
matricula = 5418
print(f'Mi coche es {color} y con matrícula {matricula}')

# Operadores matemáticos

x = 7
y = 2
print(f'{x} dividido al suelo por {y} es igual a {x//y}')
print(f'{x} módulo de  {y} es igual a {x%y}')
print(f'{x} elevado a {y} es igual a {x**y}')
print(f'la raiz cuadrada de {x} es igual a {x**0.5}')

# Redondeo
resultado = 90/7
print(resultado, round(resultado, 2), type(round(resultado, 2)), round(resultado), type(round(resultado)))




