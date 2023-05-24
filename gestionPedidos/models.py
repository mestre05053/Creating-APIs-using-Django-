from django.db import models

class Clientes(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	address=models.EmailField(max_length=50)
	phone=models.CharField(max_length=11)


class Articulos(models.Model):
	name=models.CharField(max_length=30)
	section=models.CharField(max_length=30)
	price=models.FloatField()

	def __str__(self):
		return(f"{self.name}")
	
class Pedidos(models.Model):
	number=models.IntegerField()
	section=models.CharField(max_length=30)
	price=models.FloatField()