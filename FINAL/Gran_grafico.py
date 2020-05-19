class Letra(object):
	def __init__(self, Palo, Ficha, Posicion , Turno):
		self.ficha = Ficha
		self.posicion =  Posicion
		self.palo = Palo
		self.turno = Turno
	def __str__(self):
		return "("+ self.palo +","+ self.ficha +","+ self.posicion +","+ self.turno +")"

def CodGraf(l):
	res=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
	for q in l:
		P = q[1:3]
		F = q[4]
		PO=q[6:12]
		PO=PO.replace(",","")
		T =q[-2]
		if T=="1":
			if F=="1":
				res[0]=Letra(P,F,PO,T)
			elif F=="2":
				res[1]=Letra(P,F,PO,T)
			else:
				res[2]=Letra(P,F,PO,T)
		elif T=="2":
			if F=="1":
				res[3]=Letra(P,F,PO,T)
			elif F=="2":
				res[4]=Letra(P,F,PO,T)
			else:
				res[5]=Letra(P,F,PO,T)
		elif T=="3":
			if F=="1":
				res[6]=Letra(P,F,PO,T)
			elif F=="2":
				res[7]=Letra(P,F,PO,T)
			else:
				res[8]=Letra(P,F,PO,T)
		elif T=="4":
			if F=="1":
				res[9]=Letra(P,F,PO,T)
			elif F=="2":
				res[10]=Letra(P,F,PO,T)
			else:
				res[11]=Letra(P,F,PO,T)
		elif T=="5":
			if F=="1":
				res[12]=Letra(P,F,PO,T)
			elif F=="2":
				res[13]=Letra(P,F,PO,T)
			else:
				res[14]=Letra(P,F,PO,T)
		elif T=="6":
			if F=="1":
				res[15]=Letra(P,F,PO,T)
			elif F=="2":
				res[16]=Letra(P,F,PO,T)
			else:
				res[17]=Letra(P,F,PO,T)
		elif T=="7":
			if F=="1":
				res[18]=Letra(P,F,PO,T)
			elif F=="2":
				res[19]=Letra(P,F,PO,T)
			else:
				res[20]=Letra(P,F,PO,T)
		elif T=="8":
			if F=="1":
				res[21]=Letra(P,F,PO,T)
			elif F=="2":
				res[22]=Letra(P,F,PO,T)
			else:
				res[23]=Letra(P,F,PO,T)
	return res 
	
def Tablero():
	print(" "*7+"Tablero\n")
	print("    |     |     |   ")
	print("    |     |     |   ")
	print("    |     |     |   ")
	print("    |     |     |   ")
	print("|"+"T"*19+"|")

def crear_H():
	print("\n")
	print(" "*8+"Inicio"+"\n")
	print("    |     |     |   ")
	print("    1     |     |   ")
	print("   222    |     |   ")
	print("  33333   |     |   ")
	print("|"+"T"*19+"|")


def Mov(x,lf):
	print("\n")
	print(" "*6+x+"\n")
	print("    |     |     |   ")
	ar="    #     !     ?   "
	me="   !#!   ?#?   $#$  "
	ab="  ?!#!? !?#?! ?$#$? "
	for q in lf:
		if q.ficha == "1":
			if q.posicion == "Arriba":
				if q.palo == "PA":
					ar=ar.replace("#", "1")
				elif q.palo == "PB":
					ar=ar.replace("!", "1")
				elif q.palo == "PC":
					ar=ar.replace("?", "1")

			elif q.posicion == "Medio":
				if q.palo == "PA":
					ar="    |     |     |   "
					me=me.replace("!#!", " 1 ")
				elif q.palo == "PB":
					ar="    |     |     |   "
					me=me.replace("?#?", " 1 ")
				elif q.palo == "PC":
					ar="    |     |     |   "
					me=me.replace("$#$", " 1 ")
			elif q.posicion == "Abajo":
				if q.palo == "PA":
					ar="    |     |     |   "
					ab=ab.replace("?!#!?", "  1  ")
				elif q.palo == "PB":
					ar="    |     |     |   "
					ab=ab.replace("!?#?!", "  1  ")
				elif q.palo == "PC":
					ar="    |     |     |   "
					ab=ab.replace("?$#$?", "  1  ")
		elif q.ficha == "2":
			if q.posicion == "Medio":
				if q.palo == "PA":
					me=me.replace("!#!", "222")
				elif q.palo == "PB":
					me=me.replace("?#?", "222")
				elif q.palo == "PC":
					me=me.replace("$#$", "222")

			elif q.posicion == "Abajo":
				if q.palo == "PA":
					ab=ab.replace("?!#!?", " 222 ")
				elif q.palo == "PB":
					ab=ab.replace("!?#?!", " 222 ")
				elif q.palo == "PC":
					ab=ab.replace("?$#$?", " 222 ")
		elif q.ficha == "3":
			if q.posicion == "Abajo":
				if q.palo == "PA":
					ab=ab.replace("?!#!?", "33333")
				elif q.palo == "PB":
					ab=ab.replace("!?#?!", "33333")
				elif q.palo == "PC":
					ab=ab.replace("?$#$?", "33333")

	ar=ar.replace("#","|")
	ar=ar.replace("!","|")
	ar=ar.replace("?","|")
	me=me.replace("#","|")
	me=me.replace("!"," ")
	me=me.replace("?"," ")
	me=me.replace("$"," ")
	ab=ab.replace("#","|")
	ab=ab.replace("!"," ")
	ab=ab.replace("?"," ")
	ab=ab.replace("$"," ")


	print(ar)
	print(me)
	print(ab)
	print("|"+"T"*19+"|\n")
"""
lista=["(PA,1,Arriba,1)","(PA,2,Medio,1)","(PA,3,Abajo,1)","(PA,3,Abajo,2)","(PA,2,Medio,2)","(PA,1,Arriba,2)","(PA,3,Abajo,3)","(PA,2,Medio,3)","(PC,1,Abajo,3)","(PC,1,Abajo,4)","(PA,3,Abajo,4)","(PB,2,Abajo,4)","(PB,1,Medio,5)","(PA,3,Abajo,5)","(PB,2,Abajo,5)","(PB,2,Abajo,6)","(PB,1,Medio,6)","(PC,3,Abajo,6)","(PC,3,Abajo,7)","(PC,1,Arriba,7)","(PB,2,Abajo,7)","(PC,1,Arriba,8)","(PC,2,Medio,8)","(PC,3,Abajo,8)"]
res= CodGraf(lista)
for q in res:
	print(q)
"""
def fin(l)
	Mov0=[res[0],res[1],res[2]]
	Mov1=[res[3],res[4],res[5]]
	Mov2=[res[6],res[7],res[8]]
	Mov3=[res[9],res[10],res[11]]
	Mov4=[res[12],res[13],res[14]]
	Mov5=[res[15],res[16],res[17]]
	Mov6=[res[18],res[19],res[20]]
	Mov7=[res[21],res[22],res[23]]

	Mov("Inicial",Mov0)
	Mov("Movimiento 1",Mov1)
	Mov("Movimiento 2",Mov2)
	Mov("Movimiento 3",Mov3)
	Mov("Movimiento 4",Mov4)
	Mov("Movimiento 5",Mov5)
	Mov("Movimiento 6",Mov6)
	Mov("Movimiento 7",Mov7)
