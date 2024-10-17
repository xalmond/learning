# El ahorcado
import random

def pedir_letra():
    letra = ''
    while (letra < 'A' or letra > 'Z') or len(letra) != 1:
        letra = input('Introduce una letra: ').upper()
    return letra

def letra_valida(palabra, letra):
    if letra in palabra:
        return True
    else:
        return False


lista = ['perro', 'gato', 'vaca', 'cerdo', 'caballo', 'oveja', 'mono', 'ratón', 'rata', 'tigre', 'conejo', 'dragón', 'ciervo', 'rana', 'león', 'jirafa', 'elefante', 'pájaro', 'gallina', 'gorrión', 'cuervo', 'águila', 'halcón', 'pez', 'camarón', 'langosta', 'sardina', 'atún', 'calamar', 'pulpo', 'insecto', 'bicho', 'mariposa', 'polilla', 'saltamontes', 'araña', 'mosca', 'mosquito', 'cucaracha', 'caracol', 'babosa', 'lombriz', 'marisco', 'molusco', 'lagarto', 'serpiente', 'cocodrilo']
# Normalizando lista
for i, v in enumerate(lista):
    lista[i] = lista[i].replace('á', 'a')
    lista[i] = lista[i].replace('é', 'e')
    lista[i] = lista[i].replace('í', 'i')
    lista[i] = lista[i].replace('ó', 'o')
    lista[i] = lista[i].replace('ú', 'u')
    lista[i] = lista[i].upper()
# Eligiendo una palabra
palabra_secreta = random.choice(lista)
palabra_elegida = '-' * len(palabra_secreta)

# Init variables
vidas = 6
letras_incorrectas = []

# Iteramos según vidas y estado de la palabra elegida
while vidas > 0 and palabra_secreta != palabra_elegida:
    # Pedimos letra
    letra_elegida = pedir_letra()
    # Si está en la palabra secreta moodificamos la palabra elegida
    if letra_valida(palabra_secreta, letra_elegida):
        for i, v in enumerate(palabra_secreta):
            if letra_elegida == palabra_secreta[i]:
                lista_elegida = list(palabra_elegida)
                lista_elegida[i] = letra_elegida
                palabra_elegida = ''.join(lista_elegida)
    # Si no está descontamos una vida
    else:
        if letra_elegida not in letras_incorrectas:
            letras_incorrectas.append(letra_elegida)
            vidas -= 1
    print()
    print(' '.join(list(palabra_elegida)))
    print(f'Te quedan {vidas} vidas y estas son las letras incorrectas usadas: {letras_incorrectas}')
    print()

print()
if palabra_elegida == palabra_secreta:
    print(f'Enhorabuena, has conseguido descubrir la palabra secreta: {palabra_secreta}')
else:
    print(f'Lo siento, no has conseguido descubrir la palabra secreta: {palabra_secreta}')