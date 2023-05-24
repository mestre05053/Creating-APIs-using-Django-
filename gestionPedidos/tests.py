from django.test import TestCase
from .models import Articulos

# Create your tests here.
'''
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