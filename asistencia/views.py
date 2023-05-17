from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.template import Template, Context

class Persona(object):

	"""docstring for Persona"""

	def __init__(self, nombre, apellido):
		self.nombre=nombre
		self.apellido = apellido


def saludo(request):
	temas=['Templates','Modelos','Formularios','Vistas','Despliegue']
	p1=Persona('alejandro','mestre')
	name='juyan'
	last_name='majao'
	fecha_actual = datetime.datetime.now()
	context = {}
	doc_externo=open('./asistencia/templates/index.html')
	plt=Template(doc_externo.read())
	doc_externo.close()
	#ctx=Context({'name_person':name,'last_name':last_name,'fecha_actual':fecha_actual})
	
	'''Uso la clase Persona para pasarle datos a la vista a traves de las propiedas del objeto
	persona que cree en p1'''
	ctx=Context({'name_person':p1.nombre,'last_name':p1.apellido,'fecha_actual':fecha_actual,'temas':temas})
	
	html=plt.render(ctx)

	return HttpResponse(html)


def despedida(request):

	return HttpResponse('Adios Feo')

def hora(request):
	
	fecha_actual = datetime.datetime.now()
	html='<html><body><h1>Hola Feo %s </h1></body></html>'% fecha_actual

	return HttpResponse(html)

# paso dos parametros a traves de la url
def calcula_edad(request,anno,edad_actual):

	periodo = anno - 2023
	edad_futura=edad_actual + periodo 
	html='<html><body><h1>En el año %s tendras %s años </h1></body></html>'%(anno,edad_futura)


	return HttpResponse(html)