letrasProposicionales = [chr(i) for i in range(256, 1000)]
conectivos = ['Y', 'O', '>',"@"]
#letrasProposicionales = [chr(i) for i in range(97, 106)]


class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula

	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def String2Tree(A):
	# Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
	# Input: - A, lista de caracteres con una formula escrita en notacion polaca inversa
	#        - letrasProposicionales, lista de letras proposicionales
	#        - conectivos, lista de conectivos
	# Output: formula como tree
	pila = []
	for c in A:
		# print("Examinando " + str(c))
		if c in letrasProposicionales:
			# print(u"El símbolo es letra proposicional")
			pila.append(Tree(c, None, None))
		elif c == '-':
			# print("Negamos")
			formulaAux = Tree(c, None, pila[-1])
			del pila[-1]
			pila.append(formulaAux)
		elif c in conectivos:
			# print("Unimos mediante conectivo")
			formulaAux = Tree(c, pila[-1], pila[-2])
			del pila[-1]
			del pila[-1]
			pila.append(formulaAux)
		else:
			print(u"Hay un problema: el símbolo " + str(c) + " no se reconoce")
	return pila[-1]

def V_I(A, I):
    # Devuelve el valor de verdad de A bajo la interpretación I
    # Input: - A, una fórmula en formato tree
    #        - I, una interpretación en forma de un diccionario
    # Output: 0 o 1
    if A.right == None:
        return I[A.label]
    elif A.label == '-':
        return 1 - V_I(A.right, I)
    elif A.label in ['>', 'Y', 'O']:
        if A.label == 'Y':
            return V_I(A.left, I) * V_I(A.right, I)
        elif A.label == 'O':
            return max(V_I(A.left, I), V_I(A.right, I))
        elif A.label == '>':
            return max(1 - V_I(A.left, I), V_I(A.right, I))
    else:
        print("Creo que no conozco el conectivo " + str(A.label))

def crear_interpretaciones():
    # Crea una lista con todas las interpretaciones posibles para las letrasProposicionales
    # Input: letrasProposicionales, lista de letras proposiconales
    # Output: lista de interpretaciones como diccionarios
    interps = [] # lista que se llenara con todas las posibles interpretaciones (diccionarios)

    aux = {} # primera interpretacion

    for a in letrasProposicionales:
      aux[a] = 1 # inicializamos la primera interpretacion con todo verdadero

    interps.append(aux) # ... y la incluimos en interps

    for a in letrasProposicionales:

        interps_aux = [i for i in interps] # lista auxiliar de nuevas interpretaciones

        for i in interps_aux:

            aux1 = {} # diccionario auxiliar para crear nueva interpretacion

            for b in letrasProposicionales:

                if a == b:
                    aux1[b] = 1 - i[b] # Cambia el valor de verdad para b
                else:
                    aux1[b] = i[b] # ... y mantiene el valor de verdad para las demas letras

            interps.append(aux1) # Incluye la nueva interpretacion en la lista

    return interps

def Encuentra_Interpretaciones(A):
    # Devuelve las interpretaciones que hacen verdadera a A
    # Input: - A, una fórmula en formato tree
    #        - letrasProposicionales, una lista de letras proposicionales
    # Output: lista de interpretaciones

    interps = crear_interpretaciones()
    # print("Se han creado " + str(len(interps)) + " interpretaciones.")

    lst = []
    for i in interps:
        if V_I(A, i) == 1:
            lst.append(i)

    # print("Hay " + str(len(lst)) + " interpretaciones que hacen verdadera a " + fa.Inorder(A))
    # for i in lst:
    #     print(i)
    return lst

def tablasVerdadSAT(A):
    # Devuelve las interpretaciones que hacen verdadera a A
    # Input: - A, una fórmula en formato tree
    #        - letrasProposicionales, una lista de letras proposicionales
    # Output: lista de interpretaciones

    interps = crear_interpretaciones()
    # print("Se han creado " + str(len(interps)) + " interpretaciones.")

    lst = []
    for i in interps:
        if V_I(A, i) == 1:
            return "Satisfacible"

    return "Insatisfacible"