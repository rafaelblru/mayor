#!/usr/bin/env python
#-*- coding: utf-8 -*-
mayor = 0
num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas): '))
while num >=0:
	
	if num > mayor:
		mayor = num
		
	num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas): '))	

if mayor > 0:
	print "El mayor del chorro números es " + str(mayor)
		
if mayor <= 0:
	print "Mete algun numero positivo primero si no no tiene gracia"		


