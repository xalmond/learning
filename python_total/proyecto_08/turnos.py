def generador_numeros():
    numero = 0
    while numero >= 0:
        numero += 1
        yield numero

numero_perfumeria = generador_numeros()
numero_drogueria = generador_numeros()

print(next(numero_perfumeria))
print(next(numero_perfumeria))
print(next(numero_perfumeria))
print(next(numero_drogueria))
print(next(numero_perfumeria))