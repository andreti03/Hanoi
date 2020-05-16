import Generador_Reglas as G
import Algoritmos as A
import Codificacion as C
import FNC as F
import DPLL as D
#import DPLLj as D
import sys
sys.setrecursionlimit(10000) # Para incrementar el limite de la recursion
letrasProposicionales = [chr(i) for i in range(256, 400)]

# Solicita condicion inicial


print("Creando reglas...")
reglas = G.REGLA5()

T = A.String2Tree(reglas)
print(T)
IT = A.Inorder(T)
print(IT)
TS = F.Tseitin(IT,letrasProposicionales)
print(TS)
CL= F.Clausula(TS)
l=D.conjunto_de_formulas(TS)
print(l)
print("#"*60)
Respuesta=D.DPLL(l,{})
print(Respuesta)
ID = Respuesta[1]
I = C.Decodificar(ID)
print(I)

print('Visualizaciones guardadas en /Soluciones')
print('Terminado!')
