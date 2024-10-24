# Módulos y paquetes

from practica_08_package import suma_y_resta
from practica_08_package.practica_08_subpackage import multiplicar_y_dividir

print(suma_y_resta.sumar(2, 7), suma_y_resta.restar(2, 7))
print(multiplicar_y_dividir.multiplicar(2, 7), multiplicar_y_dividir.dividir(2, 7))