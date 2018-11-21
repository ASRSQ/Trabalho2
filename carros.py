v=[0]*50
for i in range(50):
	v[i]=[0]*3
	for j in range(3):
		v[i][j]=[0]*12
		for k in range(12):
			v[i][j][k]=["0"]*30
			for x in range(30):
				v[i][j][k][x]=["0"]*30
at=[0]*50
for i in range(50):
	at[i]=[0]*5
el=0
kk=[0]*5
class carros:
	def __init__(self,marca,modelo,ano,vdia,disp,codi,dias,loca,res) :
		self.marca= marca
		self.modelo=modelo
		self.ano= ano
		self.vdia=vdia
		self.disp=disp 
		self.codi=codi
		self.dias=dias
		self.loca=loca
		self.res=res
	
	def reserva1(self,b,a,n,h):
		global v,el

		l=0
		el=0
		o=int(b/100)
		if int(o%1000)==2018:
			l=0
		if int(o%1000)==2019:
			l=1	
		i=0
		if v[h][l][int(b%100-1)][int(o/10000)-1]!=1:
			while i<int(n):
				mo=int(o/10000)+i
				if (int(b%100)-1)==11:
					if mo>30:
						if v[h][1][0][mo-30]==1:
							el=1
					else:
						if v[h][l][int(b%100)-1][int(o/10000)+i-1]==1:
							el=1		
				else:
					if mo>30:
						if v[h][l][int(b%100)][mo-30]==1:
							el=1			
					else:
						if v[h][l][int(b%100-1)][int(o/10000)+i-1]==1:
							el=1		
				i+=1
			if el==0:
				i=0
				while i<int(n):
					mo=int(o/10000)+i
					if (int(b%100)-1)==11:
						if mo>30:
							v[h][1][0][mo-30][mo-30]=a
							v[h][1][0][mo-30]=1
						else:
							v[h][l][int(b%100-1)][int(o/10000)+i-1][int(o/10000)+i-1]=a
							v[h][l][int(b%100-1)][int(o/10000)+i-1]=1

					else:
						if mo>30:
							v[h][l][int(b%100)][mo-30][mo-30]=a
							v[h][l][int(b%100)][mo-30]=1			
						else:
							v[h][l][int(b%100-1)][int(o/10000)+i-1]=1
					i+=1	


		else:
			return 0
	def reservado(self,b,n,h,r):
		global at,kk
		s=[0]*5
		s[kk[h]]=b
		j=0
		while j<r :
			if int((s[j]/100)%1000)==int((s[j+1]/100)%1000):
				if int(s[j]%100)==int(s[j+1]%100):
					if int((s[j]/100)/1000)>int((s[j+1]/100)/1000):
						at[h][j+1]=s[j]
						at[h][j]=s[j+1]

					else:
						at[h][j]=s[j]
						at[h][j+1]=s[j+1]

				elif	int(s[j]%100)>int(s[j+1]%100):
					at[h][j]=s[j+1]
					at[h][j+1]=s[j]
				else :
					at[h][j]=s[j]
					at[h][j+1]=s[j+1]
			else:
				at[h][j]=s[j]
			j+=1
		kk[h]+=1

	def Preservado(self,i,h):
		global at
		print(at[h][i])








	def devolver(self,b,a,n,h):

		l=0
		el=0
		o=int(b/100)
		if int(o%1000)==2018:
			l=0
		if int(o%1000)==2019:
			l=1	
		i=0
		while i<int(n):
					mo=int(o/10000)+i
					if (int(b%100)-1)==11:
						if mo>30:
							v[h][1][0][mo-30][mo-30]=a
							v[h][1][0][mo-30]=0
						else:
							v[h][l][int(b%100-1)][int(o/10000)+i-1][int(o/10000)+i-1]=a
							v[h][l][int(b%100-1)][int(o/10000)+i-1]=0

					else:
						if mo>30:
							ç=0
							#v[h][l][int(b%100)][mo-30]=0			
						else:
							v[h][l][int(b%100-1)][int(o/10000)+i-1]=0
					i+=1	

	def printStatus(self,b,h):
		global v
		l=0
		o=int(b/100)
		if int(o%1000)==2018:
			l=0
		if int(o%1000)==2019:
			l=1

		return v[h][l][int(b%100-1)][int(o/10000-1)]
	def printClient(self,b,h):
		global v
		l=0
		o=int(b/100)
		if int(o%1000)==2018:
			l=0
		if int(o%1000)==2019:
			l=1

		return str(v[h][l][int(b%100-1)][int(o/10000-1)][int(o/10000-1)])
	def dispo(self):
			global el
			return el	

		







