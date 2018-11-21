import os,sys
from datetime import datetime
from carros import carros
c=[]
i=0
veículos="001"
limpa	= "os.system('cls' if os.name == 'nt' else 'clear')"
now = datetime.now()
dia=now.day
mes=now.month
ano=now.year
al=0
at=0
vdc=[0]*50
reservado=[0]*50
reso=[0]*50
for j in range(50):
	reso[j]=[0]*5
	for k in range(5):
		reso[j][k]=[0]*5

h=[0]*50
def stt(c):
	if c==1:
		u="Disponível"
	if c==2:
		u="Alugado"
	if c==3:
		u="Reservado"
	if c==4:
		u="Atrasado"
	if c==5:
		u="Excluido"			
	return u
def eReserva():
	global c,reso,dia,mes,ano,al,h,vdc
	k=dia*1000000+ano*100+mes
	j=0
	while j<len(c):
		i=0
		while i<5:
			if reso[j][i]==k:
				al=al+1
				c[j].disp=2
				c[j].res=vdc[j]
				h[j]=0


			i+=1
		j+=1


def res(b,a,u,t):
	global c,h,reservado,reso,vdc
	if c[int(a)-1].printStatus(b,int(a)-1)==1:
		print("Data não disponível")
		input()
	else:
		if c[int(a)-1].reserva1(b,t,u,int(a)-1)== 0:
			print("	Data não disponível")
			input()
		elif c[int(a)-1].dispo()==1:
			print("A quantidade de dias selecionada não está disponível")
			input()
		else:
			c[int(a)-1].reserva1(b,t,u,int(a)-1)
			if c[int(a)-1].disp!=2 and c[int(a)-1].disp!=4:
				c[int(a)-1].disp=3
				c[int(a)-1].loca=t
				#reso[int(a)-1][reservado[int(a)-1]][0]=int(u)
				reso[int(a)-1][reservado[int(a)-1]]=b
				vdc[int(a)-1]=u
				#reso[int(a)-1][reservado[int(a)-1]][reservado[int(a)-1]]=t
				#eReserva(t)
				reservado[int(a)-1]=reservado[int(a)-1]+1




			
h=[0]*50

def atraso():
	global c,h,at
	i=0
	while i<len(c):
		if c[i].res!=200:
			h[i]+=1
			if h[i]>int(c[i].res)-1:
				if h[i]==int(c[i].res) :
					at+=1
					c[i].disp=4
		i+=1


						
#def devolver():

def status():
	print(" Cadastros:",i,"       Alugueis:",al,"        Atrassos:",at,"    ")
	print("|=====================================================|")
def inicial():
	eval(limpa)
	cabecalho()
	status()
	corpo()
	roda()
	escolha()
def cabecalho():
	print("|=====================================================|")
	print("|               ALUGUEL DE CARROS                     |")
	print("|=====================================================|")
def corpo():
	print("                                                       ")
	print(" 1-Consultar veículos       	5-Excluir veículos        ")	
	print(" 2-Adicionar veículos       	6-Avançar data atual      ")
	print(" 3-Alugar/reservar veículos 	7-Sair                    ")	
	print(" 4-Devolver/liberar veículos                           ")			
def roda():
	print("|=====================================================|")
	print("  Data:",ano,"/",mes,"/",dia,"       Hora:",now.hour,":",now.minute ,"           ")
	print("|=====================================================|")
def escolha():
	a=input(" Digite um número de 1-7 para escolher uma das opções:")
	if a=="1" or a=="2" or a=="3" or a=="4" or a=="5" or a=="6" or a=="7":
		if a=="1":
			eval(limpa)
			cv()
		if a=="2":
			eval(limpa)
			addv()	
		if a=="3":
			eval(limpa)
			alv()
		if a=="4":
			dv()
			eval(limpa)
		if a=="6":
			avancar()
		if a=="5":
			exv()	
		if a=="7":
		 	 sys.exit()
	else:
		print("Digite um comando válido")
		input()
		inicial()	 	 
		 	 

def cv():
	global c
	i=0
	cabecalho()
	while i != len(c):			
		print(" Código",c[i].codi," Veículo:",c[i].modelo,"Status:",stt(c[i].disp))
		i+=1
	s=input(" Para saber mais detalhes sobre o carro basta digitar o seu código:")
	if int(s)<=len(c):
		if c[int(s)-1].disp!=5:
				eval(limpa)
				cabecalho()
				print("	Veículo de código:",c[int(s)-1].codi)
				print("	Marca:",c[int(s)-1].marca)
				print("	Modelo:",c[int(s)-1].modelo)
				print("	Ano:",c[int(s)-1].ano)
				print("	Preço do aluguel:",c[int(s)-1].vdia)
				input()
				inicial()
		else:
			print("Veículo Excluido")
			input()
			inicial()
					
	else:
		print(" Número não cadastrado ")
		input()
		inicial()		
def addv():
	global veículos
	global c
	global i
	cabecalho()
	print(" Digite a marca do veiculo:                            ")
	a=input(" ")
	print(" Digite o modelo do veiculo:                           ")
	b=input(" ")	
	print(" Digite o ano do veiculo:                               ")
	l=int(input(" "))
	print(" Digite o valor da diária do veículo:")
	d=float(input(" "))
	veículos= ("00"+str(i+1))
	c.append(carros(a,b,l,d,1,veículos,9999999,"9999",200))
	i+=1
	a=1
	eval(limpa)
	inicial()
def alv():
	global al,c,dia,mes,ano
	b=0
	cabecalho()
	t=input(" Para alugar digite 1 para reservar digite 2:")
	if t=="1":
		eval(limpa)
		cabecalho()
		print(" Digite o número do veículo que será alugado :")
		s=input(" ")
		if int(s)<=len(c):
			if c[int(s)-1].disp==1 or c[int(s)-1].disp==3:
				print(" Digite o nome do Locatário:                          ")
				a=input(" ")
				print(" Digite a quantidade de dias:                         ")
				b=input(" ")
				if int(b)>30:
					print(" Número de dias não permitido na locadora")
				else:
					c[int(s)-1].disp=2
					al+=1
					k=dia*1000000+ano*100+mes
					c[int(s)-1].reserva1(k,a,b,int(s)-1)
					if c[int(s)-1].dispo()==1:
						print(" A quantidade de dias selecionada não está disponível")
						input()
					else:
						c[int(s)-1].reserva1(k,a,b,int(s)-1)
						c[int(s)-1].res=b
						c[int(s)-1].loca=a
						input()

						
				inicial()                    
			else: 
				print(" Veículo não Disponível")
				input()
				inicial()
		else:
			print(" Veículo não cadastrado")
			input()
			inicial()	

	if t=="2":
		eval(limpa)
		cabecalho()
		print(" Digite o número do veículo que será reservado :")
		a=input(" ")
		print(" Digite o nome do Locatário :")
		t=input(" ")
		print(" Digite a data da reserva :")
		b=input(" ")
		print(" Digite a quantidade de dias que o cliente passará com o carro:")
		h=input(" ")
		if int(a)<=len(c):
			if c[int(a)-1].disp==1 or c[int(a)-1].disp==3:
				if int(h)>30:
					print(" Número de dias não permitido na locadora")
					input()
				else:
					res(int(b),int(a),int(h),t)
			else:
				print("	Veículo não disponível")

		else:
			print(" Veículo não cadastrado")
			input()
			inicial()	
		inicial()

def dv():
	eval(limpa)
	cabecalho()
	global dia,mes,c,h,al,at,ano
	i=0
	while i != len(c):
		if c[i].disp==2 or c[i].disp==3:
			k=dia*1000000+ano*100+mes			
			print(" Código",c[i].codi," Veículo:",c[i].modelo,"Status:",stt(c[i].disp),"Locatário:",c[i].loca)
		i+=1
	print(" Digite 1 para devolver e 2 para liberar os veiculos:")
	go= input(" ")
	if go=="1":
		print(" Digite o número do veículo que será devolvido:")
		a=input(" ")
		if int(a)<=len(c):
			if c[int(a)-1].disp==4:
				y=float(c[int(a)-1].res)
				o=float(c[int(a)-1].res)-1
				x=float(c[int(a)-1].vdia)
				k=float(h[int(a)-1])-o
				w=k*2*x
				j=x*y
				print(" O valor da divida é:",w+j)
				print(" Veiculo devolvido")
				c[int(a)-1].disp=1
				c[int(a)-1].res=0
				h[int(a)-1]=0
				al=al-1
				at=at-1
				input()
				inicial()
			if c[int(a)-1].disp==2:
				if int(c[int(a)-1].res)>int(h[int(a)-1]):
					x=float(c[int(a)-1].vdia)
					u=float(c[int(a)-1].res)-float(h[int(a)-1])
					print(" A divida é:",(h[int(a)-1]+1)*x)
					print(" Veiculo devolvido")
					k=dia*1000000+ano*100+mes
					c[int(a)-1].disp=1
					h[int(a)-1]=0
					c[int(a)-1].res=0
					al=al-1
					c[int(a)-1].devolver(k,"0",u,int(a)-1)
					input()
					inicial()
				else:
					x=float(c[int(a)-1].vdia)
					print(" A divida é:",(float(c[int(a)-1].res*x)))
					print(" Veiculo devolvido")
					input()
					c[int(a)-1].disp=1
					c[int(a)-1].res=0
					h[int(a)-1]=0
					al=al-1
					inicial()
			else:
				print("Veículo não está alugado ou reservado")
				input()
				inicial()
	if go=="2":
		print(" Digite o número do veículo que será liberado:")
		a=input(" ")
		u=float(c[int(a)-1].res)-float(h[int(a)-1])
		k=dia*1000000+ano*100+mes
		if c[int(a)-1].disp==2 or c[int(a)-1].disp==3:
			c[int(a)-1].disp=1
			h[int(a)-1]=0
			if c[int(a)-1].disp==2:
				al=al-1
			c[int(a)-1].devolver(k,"0",c[int(a)-1].res,int(a)-1)
		else:
			print("Este veículo não pode ser liberado")
			input()	

		inicial()

def exv():
	global c
	eval(limpa)
	cabecalho()
	print(" Digite o codigo do veiculo que deseja excluir:")
	a=input(" ")
	if int(a)<=len(c):
		if c[int(a)-1].disp==1:
			c[int(a)-1].disp=5
			inicial()
		else:
			print(" Veículo não pode ser excluido")
			input()
			inicial()	
	else:
		print("Veículo não cadastrado")
		inicial()









		

		

def avancar():
	global dia,ano,mes
	atraso()
	if dia<30:
		dia+=1
	else:
		dia=1
		mes+=1	
	k=(dia)*1000000+ano*100+mes
	u=k%100
	if u>12:
		mes=1
		k=k+90
		ano+=1
	eReserva()						
	inicial()
def main():
	inicial()
main()	
