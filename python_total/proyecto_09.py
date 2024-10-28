# Buscador de números de serie

import datetime
import time
import math
import os
import re

print('-' * 52)
print(f"Fecha de búsqueda: {datetime.date.today().strftime('%d/%m/%y')}")
print()
print('ARCHIVO\t\t\tNRO. SERIE')
print('-------\t\t\t-------------')
found_num = 0
time_start = time.time()
for i in os.walk('data\\proyecto_09\\Mi_Gran_Directorio'):
    for j in i[2]:
        my_file = open(str(i[0] + '\\' + j))
        for k in my_file.readlines():
            resultado = re.search(r'N\D{3}-\d{5}', k)
            if resultado:
                print(f'{resultado.group()}\t\t{j}')
                found_num += 1
        my_file.close()
time_end = time.time()
print()
print(f'Números encontrados: {found_num}')
print(f'Duración de la búsqueda: {math.ceil(time_end - time_start)} segundos')
print('-' * 52)