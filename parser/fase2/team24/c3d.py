from InstruccionesDGA import tabla 
from datetime import date
from InstruccionesDGA import cont 
from InstruccionesDGA import NombreDB
from tablaDGA import *
from sql import * 
import mathtrig as mt
#Funcion sql.execute

pila = []
for i in range(100):
    pila.append(i)

def ejecutar(): 
	n_db = ts.buscarIDTB(NombreDB)
	NuevoSimbolo = Simbolo(cont,'myFuncion',TIPO.FUNCTION,n_db)
	ts.agregar(NuevoSimbolo)
	cont+=1

	t1 = 'INICIO CALIFICACION FASE 2'
	pila[0] = t1
	myFuncion()
	print(pila[10])
def myFuncion():
	texto = pila[0]
	t0 = texto
	
	pila[10] = t0
	
ejecutar()