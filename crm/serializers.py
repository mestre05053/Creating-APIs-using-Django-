from .models import Record
from rest_framework import serializers

'''Esta es la clase de serializacion que convierte el objeto Record de tipo DB a 
a un objeto que la api puede leer. Carga en el MODEL de la clase meta el nombre de
 la clase de BD a la hace referecencia y le pasa en FIELDS los campos que se van a serializar'''

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone','address','city','state','zipcode']