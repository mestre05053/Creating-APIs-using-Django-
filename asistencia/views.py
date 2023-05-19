from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



class Persona(object):

	"""docstring for Persona"""

	def __init__(self, nombre, apellido):
		self.nombre=nombre
		self.apellido = apellido


def saludo(request):
	#Check to see if logging in 
	context = {}
	if request.method == 'POST':
		username =request.POST['username']
		password =request.POST['password']
		#Authenticate
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,'You have Been Logged In...')
			return redirect('saludo')
		else:
			messages.error(request,'There Was An Error Logging In, Please Try Again...')
			return redirect('saludo')
	else:
		return render(request,'index.html',context)

def json(request):
	context={}

	return render(request, 'json.html', context)

def logout_user(request):
	logout(request)
	messages.success(request,'You Have Logged Out...')
	return redirect('saludo')
