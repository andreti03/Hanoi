import Generador_Reglas as G
import Algoritmos as A
import Codificacion as C
import sys
sys.setrecursionlimit(10000) # Para incrementar el limite de la recursion

# Solicita condicion inicial


print("Creando reglas...")
reglas = G.REGLA()

T = A.String2Tree(reglas)

print('Encontrando soluciones (paciencia, por favor!)...')
listaSoluciones = A.Encuentra_Interpretaciones(T)

print('Hay', str(len(listaSoluciones)), ' interpretaciones que resuelven el problema.')
# print('Las interpretaciones son:\n', listaSoluciones)

print(listaSoluciones)

print('Visualizaciones guardadas en /Soluciones')
print('Terminado!')
