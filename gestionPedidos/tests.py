from django.test import TestCase
from django.urls import reverse
from .models import Articulos

# Create your tests here.
'''
   Las funciones TEST para que se ejecuten deben llevar como nombre la palabra ***test_***
   La clase  UrlSiteTest hereda de TESTCASE tiene la funcion test_page_status_code
   que mediante un ciclo FOR evalua el status code de cada pagina que devulve cada pagina que 
   se le pasa a lista 
'''
class UrlSiteTest(TestCase):      

    def test_page_status_code(self):
        pages =['/','/json/','/register/']
        for page in pages:
            response = self.client.get(page)
            if response.status_code == 200:
                print('Page', page, response.status_code)
            else:
                print('Page',page, response.status_code )
    
    '''
        La funcion **test_view_url_by_name** se asegura de que las paginas estan 
        en las urls que se les declaro
    '''
    def test_view_url_by_name(self):
        pages =['home','json','register','logout']
        templates =['home','json','register','logout']
        print('----------------------------------------------------------')
        for page in pages:
            response = self.client.get(reverse(page))
            if response.client.get(reverse(page)):
                print('Pagina:', page , 'se encuentra en ' ,page,'code:', response.status_code)
            else:
                print('Pagina:', page , 'no se encuentra en ',page, 'code:', response.status_code)
  
'''
   La clase  ArticulosModelTest hereda de TESTCASE tiene la funcion setUp que inicializa contenido
   en la BD ARTICULOS, luego la funcion *test_text_content* evalua si coincide en la BD el valor 
   que se le paso anteriormente.
'''

class ArticulosModelTest(TestCase):
    def setUp(self):
        Articulos.objects.create(name='celular', section='Mercado', price=10)
        
    def test_text_content(self):
        articulo=Articulos.objects.get(id=1)
        expected_object_name = f'{articulo.name}'
        expected_object_section = f'{articulo.section}'
        self.assertEqual(expected_object_name, 'celular')
        self.assertEqual(expected_object_section, 'Mercado')
    