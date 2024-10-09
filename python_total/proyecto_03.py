# Analizador de texto

texto = input('Introduce un texto: ')
letras = list(input('lista de tres letras: '))

print()
for i in (0,1,2):
    print(f'La letra {letras[i]} aparece {texto.lower().count(letras[i].lower())} veces en el texto')
print()
print(f'El texto contiene {len(texto.split())} palabras')
print()
print(f'La primera letra del texto es la {texto[0]} y la última es la {texto[-1]}')
print()
print(f'El texto en orden inverso sería:\n{" ".join(texto.split()[::-1])}')
print()
dic={True: 'Sí', False: 'No'}
print(f'{dic["python" in texto.lower()]} aparece la palabra python en el texto')
print()


