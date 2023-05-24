from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Articulos
from gestionPedidos.models import Articulos
    
'''
    Esta vista esta creada a partir de una clase esta es la otra manera de 
    hacer las vistas una es por clases otra por medio de funciones. Para hacer vistas
    basadas en clases se debe de importar ' from django.views.generic import TemplateView'
    luego se le pasa a la clase por medio de la propiedad TEMPLATE_NAME el nombre de la plantilla 
    html que va a usar.
    '''
'''
    La clase LISTVIEW es la que permite crear vistas que carguen objetos desde un modelo es
    necesario que la clase que mostrara los elementos herede de esta sino no es posible cargar 
    objetos de la BD

    '''
class HomePageView(ListView):
    model = Articulos
    template_name = 'home.html'
    context_object_name = 'articulos'

class AboutPageView(TemplateView):
    template_name = 'about.html'
    

def thor(request):
    #qs = Articulos.objects.values().order_by('-name')
    qs = Articulos.objects.all()#.order_by('-name')
    print (qs)
    return render(request, 'thor.html', {'qs':qs})

