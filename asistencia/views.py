from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.template import Template, Context

def saludo(request):
	context = {}
	doc_externo=open('./asistencia/templates/index.html')
	plt=Template(doc_externo.read())
	doc_externo.close()
	ctx=Context()
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