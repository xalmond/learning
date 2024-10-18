# Recetario
import os
from pathlib import Path


def seleccion_tarea():
    seleccion = '0'
    while seleccion not in [str(x) for x in range(1, 7)]:
        os.system('cls')
        print()
        print('[1] - Leer receta.')
        print('[2] - Crear receta.')
        print('[3] - Crear categoría.')
        print('[4] - Eliminar receta.')
        print('[5] - Eliminar categoría.')
        print('[6] - Finalizar programa.')
        print()
        seleccion = input('Cúal es tu selección: ')
    return int(seleccion)


def mostrar_elementos(lista_elementos):
    print()
    os.system('cls')
    for i, v in enumerate(lista_elementos):
        print(f'[{i + 1}] - {v.name}')
    print()


def seleccion_elemento(ruta, elemento):
    lista_elementos = list(ruta.glob('*'))
    if len(lista_elementos) == 0:
        os.system('cls')
        print()
        print('No hay ninguna receta en esta categoría')
        return ''
    else:
        seleccion = '0'
        while seleccion not in [str(x) for x in range(1, len(lista_elementos) + 1)]:
            mostrar_elementos(lista_elementos)
            seleccion = input('Cúal es tu selección: ')
        return lista_elementos[int(seleccion) - 1]


# Init variables
ruta_categorias = Path(Path.home(), 'Documents', 'learning', 'python_total', 'data', 'proyecto_06')
seleccion = 1
while seleccion in range(1, 6):
    seleccion = seleccion_tarea()
    if seleccion == 1:
        categoria = seleccion_elemento(ruta_categorias, 'categoría')
        ruta_recetas = Path(ruta_categorias, categoria)
        receta = seleccion_elemento(ruta_recetas, 'receta')
        if receta != '':
            ruta_receta = Path(ruta_recetas, receta)
            os.system('cls')
            print()
            print(ruta_receta.read_text())
        print()
        input('Presione Enter para siguiente tarea.')
    elif seleccion == 2:
        categoria = seleccion_elemento(ruta_categorias, 'categoría')
        ruta_recetas = Path(ruta_categorias, categoria)
        lista_recetas = list(ruta_recetas.glob('*'))
        mostrar_elementos(lista_recetas)
        nueva_receta = input('Cúal es el nombre de la nueva receta: ')
        ruta_receta = Path(ruta_recetas, nueva_receta + '.txt')
        nuevo_fichero = open(ruta_receta, 'w')
        nuevo_fichero.write(f'Esta es la receta de {nueva_receta}')
        nuevo_fichero.close()
    elif seleccion == 3:
        lista_categorias = list(ruta_categorias.glob('*'))
        mostrar_elementos(lista_categorias)
        nueva_categoria = input('Cúal es el nombre de la nueva categoria: ')
        ruta_categoria = Path(ruta_categorias, nueva_categoria)
        os.makedirs(ruta_categoria)
    elif seleccion == 4:
        categoria = seleccion_elemento(ruta_categorias, 'categoría')
        ruta_recetas = Path(ruta_categorias, categoria)
        receta = seleccion_elemento(ruta_recetas, 'receta')
        if receta != '':
            ruta_receta = Path(ruta_recetas, receta)
            os.remove(ruta_receta)
        else:
            print()
            input('Presione Enter para siguiente tarea.')
    elif seleccion == 5:
        categoria = seleccion_elemento(ruta_categorias, 'categoría')
        ruta_recetas = Path(ruta_categorias, categoria)
        for receta in list(ruta_recetas.glob('*')):
            os.remove(receta)
        os.rmdir(ruta_recetas)




