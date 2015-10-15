#!/usr/bin/env python
#-*- coding: utf-8 -*-
mayor = 0
print "Mete una chorra de numeros positivos y te digo cual es el mayor"
num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas): '))
while num >=0:
	
	if num > mayor:
		mayor = num
		
	num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas): '))	

if mayor > 0:	
	print "El mayor del chorro números es " + str(mayor)
else:
	print "Mete algun numero positivo primero si no no tiene gracia"		


