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