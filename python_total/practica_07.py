# Clases

class Pajaro:
    pass
mi_pajaro = Pajaro()
print()
print(mi_pajaro)
print(type(mi_pajaro))
tu_pajaro = Pajaro()
print()
print(tu_pajaro)
print(type(tu_pajaro))

# Atributos

class Pajaro:
    alas = 2
    def __init__(self, especie, color):
        self.especie = especie
        self.color = color
mi_pajaro = Pajaro('colibrí', 'verde')
print()
print(mi_pajaro)
print(f'Mi pájaro es un {mi_pajaro.especie}, es de color {mi_pajaro.color}')
print(f'y, por supuesto, tiene {mi_pajaro.alas} alas.')

# Métodos y sus tipos

class Pajaro:
    alas = 2
    def __init__(self, especie, color):
        self.especie = especie
        self.color = color

    def piar(self):
        print('pio')
    def volar(self, metros):
        print(f'El {self.especie} ha volado {metros} metros.')  # Entender diferencia entre parámetro y atributo

    # Métodos de instancia

    def pintar_negro(self):
        self.color = 'negro'  # Cambia atributos de instancia
        self.piar()  # Puede acceder a otro métodos

    # Métodos de clase

    @classmethod
    def poner_huevos(cls, cantidad):  # En vez self, cls ya que está relacionado con la clase, no con instancias
        cls.alas = 0  # Si puedo modificar atributos de clase
        print(f'Puso {cantidad} huevos con {cls.alas} alas cada uno.')

    # Métodos estáticos

    @staticmethod
    def mirar():  # No pueden acceder a atributos de instancia y clase (ni self, ni cls)
        print('00')

mi_pajaro = Pajaro('colibrí', 'verde')
print()
for i in range(5):
    mi_pajaro.piar()
mi_pajaro.volar(50)
print()
print(f'Mi pájaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}.')
mi_pajaro.pintar_negro()
print(f'Mi pájaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}.')
print()
Pajaro.poner_huevos(3)
print()
Pajaro.mirar()

otro_pajaro = Pajaro('loro', 'naranja')
print()
print(f'Mi pájaro es un {otro_pajaro.especie}, es de color {otro_pajaro.color}')
print(f'pero ahora tiene {otro_pajaro.alas} alas.')

# Herencia


class Animal():

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Ester ha emitido un sonido')

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        # self.edad = edad  # Habría que volver a escribirlos (los atributos heredados)
        # self.color = color
        super().__init__(edad, color)  # Para no tener que escribir los atributos heredados
        self.altura_vuelo = altura_vuelo  # Nuevo atributo

    def hablar(self):  # Método modificado (sobreescrito)
        print('pio')

    def volar(self, metros):  # Método nuevo (no heredado)
        print(f'El pájaro ha volado {metros} metros.')


piolin = Pajaro(2, 'naranja', 60)
print()
piolin.nacer()  # Método heredado de la clase Animal
print(piolin.edad, piolin.altura_vuelo)
piolin.hablar()
piolin.volar(100)

# MRO Metho resolution order

class Padre:
    def hablar(self):
        print('hola')
class Madre:
    def reir(self):
        print('ja ja')
    def hablar(self):
        print('Adios')
class Hijo(Madre, Padre):
    pass
class Nieto(Hijo):
    pass

print()
mi_nieto = Nieto()
mi_nieto.hablar()
print(Nieto.__mro__)

# Polimorfismos

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(f'La vaca {self.nombre} hace muuu')


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'La oveja {self.nombre} hace beee')


mi_vaca = Vaca('Estrella')
mi_oveja = Oveja('Sol')
print()
for i in [mi_vaca, mi_oveja]:  # Puedo pasar una lista de objetos !!!!!!! IMP !!!!!!!!!
     i.hablar()  # Mismo nombre de atributo de diferentes clases = Distintas acciones

# Métodos especiales


class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones


mi_cd = CD('Pink Floyd', 'The Wall', 15)
print()
print(mi_cd)
print(len(mi_cd))














