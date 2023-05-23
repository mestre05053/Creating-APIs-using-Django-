from django.shortcuts import render
from django.views.generic import TemplateView
'''
Esta vista esta creada a partir de una clase esta es la otra manera de 
hacer las vistas una es por clases otra por medio de funciones. Para hacer vistas
basadas en clases se debe de importar ' from django.views.generic import TemplateView'
luego se le pasa a la clase por medio de la propiedad TEMPLATE_NAME el nombre de la plantilla 
html que va a usar.
'''
class HomePageView(TemplateView):
    template_name = 'home.html'