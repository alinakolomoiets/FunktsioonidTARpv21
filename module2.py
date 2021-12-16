#def Kolmnurga_pindala(külg:float,kõrgus:float):
#	"""Leiab kolmnurga pindalat. On antud kõrgus ja külje pikkus.Tagastab S float formaadis
#	:param float külg:Kolmnurga külje pikkus
##	:param float kõrgus:Kõrgus vasta küljele
#	:rtype:var
##	"""
#	if külg<0 or kõrgus<0:
#		S="valed andmed!"
#	else:
#		S=0,5*külg*kõrgus
#	return S 

#def N(külg1:float,külg2:float)->float:
#def arithmetic(a:float,b:float,tehe:str):
	#"""Liitmine , lahutamine, korrutamine ja jagamine.Tagastab arv, kui vastus on arv ja "Tundmatu tehe",kui ei saa vastuat  #  #leida või sisestatud teh ei ole ["+","-","*","/"].
#	:param float a:Esimine arv 
#	:param float b:Teine arv 
#	:param str tehe :Aritmeetilise tehe 
#	:rtype:var	
#	"""
#	if tehe in ["+","-","*","/"]:
#		if tehe=="/" and b==0:
#			vastus="Div/0"
#		else:
#			vastus=eval(str(a)+tehe+str(b))
#	else:
#		vastus="Tundmatu tehe!"
#	return vastus

def Liigaasta(aasta:int)->bool:
	"""Sisestame aasta number ja tagastame True , kui aasta in liigaasta ja False ,kui ei ole.
	:param int aasta :Aasta jrk.number 
	:rtype:bool
	"""
	if aasta
from math import*
#def ruud(a:float):
#	"""
#	:rtype:float,float,float
#	"""
#	S=2**a
#	P=(a+b)*2
#	d=sqrt(2*a*a)
#	return P,S,d
#Ümbermõõt,Pinadala,Diogonaal=ruud(3)

def season(kuu:int)->str:
	"""Võtme kuu number ja tagastame tekst :Talv,Kevad, Suvi või Sügis.
	:param int:seasons
	"""
	#if a==1 or a==12 or a==2:
	#	print("talv")
	#elif a==3 or a==4 or a==5:
	#	print("kevad")
	#elif a==6 or a==7 or a==8:
	#	print("suvi")
	#elif a==9 or a==10 or a==11:
	#	print(sügis)
	while 1:
		if kuu >=1 and kuu <=12:
			if kuu in [1,2,12]:
				s="Talv"
			elif kuu in [3,4,5]:
				s="Kevad"
			elif kuu in [6,7,8]:
				s="Suvi"
			elif kuu in [9,10,11]:
					s="Sügis"
			break
		else:
			kuu=int(input("Kui:1-12"))
	return s	
def bank(a:float,years:int)->float:
	"""
	:param float a:Money
	:param str years:Years
	"""
	for i in range(years):
		a*=1.1
	return a 
#TASK6
def is_prime(arv:int)->bool:
	"""
	:param int a :arv
	"""
	n=0#число
	if arv<1000 or arv>0:
		for i in range(1,arv+1):
			arv%i==0:
				n+=1
	if n==2:
		n=True 
	else :
		n=False
	return n
