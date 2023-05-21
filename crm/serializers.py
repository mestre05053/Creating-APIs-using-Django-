from .models import Record
from rest_framework import serializers

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone','address','city','state','zipcode']