import os
import turnos


def seleccion_tarea():
    seleccion = '0'
    while seleccion not in [str(x) for x in range(1, 5)]:
        os.system('cls')
        print()
        print('[1] - Perfumería.')
        print('[2] - Farmacia.')
        print('[3] - Cosmética.')
        print('[4] - Finalizar programa.')
        print()
        seleccion = input('Cúal es tu selección: ')
    return int(seleccion)


@turnos.completar_ticket
def imprimir_turno(turno):
    os.system('cls')
    print(turno)


secciones = ['P', 'F', 'C']
nuevos_turnos = [turnos.generador_numeros(),
                 turnos.generador_numeros(),
                 turnos.generador_numeros()]
seleccion = 1
while seleccion in range(1, 4):
    seleccion = seleccion_tarea()
    if seleccion != 4:
        turno = secciones[seleccion - 1] + ' - ' + str(next(nuevos_turnos[seleccion - 1]))
        imprimir_turno(turno)



