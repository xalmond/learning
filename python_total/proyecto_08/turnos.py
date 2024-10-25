def generador_numeros():
    numero = 0
    while numero >= 0:
        numero += 1
        yield numero

def completar_ticket(funcion):
    def annadir_cortesia(turno):
        print()
        print('Su turno es:')
        funcion(turno)
        print('Aguarde y será atendido')
        print()
        input('Presione Enter para pedir nuevo número.')
    return annadir_cortesia
