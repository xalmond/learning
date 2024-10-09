# Comisiones de Ventas

nombre = input('¿Cuál es tu nombre?: ')
ventas = input('¿Cuál ha sido tu cantidad de ventas?: ')
resultado = float(ventas) * 0.13

print(f'Tu nombre es {nombre} y tus comisiones ascienden a ${round(resultado, 2)}')
