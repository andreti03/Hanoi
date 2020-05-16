letrasProposicionales = [chr(i) for i in range(256, 1000)]

archivo = open("Letras.txt", "w")

count=1
Posiciones=["Arriba","Medio","Abajo"]
Palos=["PA","PB","PC"]
Fichas=["1","2","3"]
Turnos=["1","2","3","4","5","6","7","8"]
i=0
for i in Turnos:
	for F in Fichas:
		for P in Posiciones:
			for PX in Palos:
				if F=="2" and P == "Arriba":
					break
				elif F=="3" and P == "Arriba":
					break
				elif F=="3" and P == "Medio":
					break
				W="("+PX+","+ F +","+ P +","+ i +")"
				archivo.write(W)
				archivo.write("\n")

archivo.close()

myfile = open("Letras.txt","r")
x = myfile.readlines()
myfile.close()

#print(len(letrasProposicionales))
Original={}
Inversa={}
for q in range(len(x)):
	x[q]=x[q].replace("\n","")
	Original[x[q]]=letrasProposicionales[q]
	
for q in range(len(x)):
	x[q]=x[q].replace("\n","")
	Inversa[letrasProposicionales[q]]=x[q]

#print("Original ->",Original)
#print("Inversa ->",Inversa)
#k = Original.get("(PA,3,Abajo,8)")
#print(k)

def Codificacion(s):
	s=s.replace(" ","")
	for q in s:
		p = s.find("(")
		f = s.find(")")
		rem = s[p:f+1]
		if rem=="":
			return s
		l = Original.get(rem)
		s=s.replace(rem,l)
	return s
