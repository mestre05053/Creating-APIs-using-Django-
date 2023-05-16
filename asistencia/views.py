from django.http import HttpResponse
import datetime

def saludo(request):

	html='<html><body><h1>Hola Feo</h1></body></html>'

	return HttpResponse(html)


def despedida(request):

	return HttpResponse('Adios Feo')

def hora(request):
	
	fecha_actual = datetime.datetime.now()
	html='<html><body><h1>Hola Feo %s </h1></body></html>'% fecha_actual



	return HttpResponse(html)