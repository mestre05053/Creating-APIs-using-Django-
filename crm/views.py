from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm, CreateRecordForm
from .models import Record

###API imports
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecordSerializer


''' Hay varias maneras de hacer una API se puede hacer utiizando 
	Clases o Funciones en este caso utlize Clases siguiendo el tutorial
	de Django-Rest-Framework. 
	Esta clase carga en un objeto de ViewSet el Modelo de la BD, 
'''
class RecordViewSet(viewsets.ModelViewSet):     
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Record.objects.all().order_by('created_at')
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticated]


'''La funcion SALUDO corresponde a la pagina index del sitio
	chequea siempre si usuario se autentifico sino solicita user y passwd
'''
def saludo(request):
	context={}
	#Check to see if logging in 
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
'''La funcion JSON es la que carga de la BD el objeto RECORD 

'''
def json(request):
	if request.user.is_authenticated:
		records = Record.objects.all()
		context = {'records':records}
		return render(request, 'json.html', context)
	else:
		messages.error(request, 'You Must Be Authenticated To Access Here!...')
		return redirect('saludo')

def logout_user(request):
	logout(request)
	messages.success(request,'You Have Logged Out...')
	return redirect('saludo')

	'''
	La funcion REGISTER_USER carga el formulario SignUpForm con la request. POST 
	valida y salva la forma ,luego carga de la informacion limpia del formulario
	el usuario y la contrasenna. Luego le pasa estos dos valores a la funcion AUTHENTICATE()
	y los guarda en la variable USER y le pasa a la funcion LOGIN() la request y la variable USER
	para luego de registrar al usuario autenticarlo
	'''
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			#Authenticate and Logging
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password=password)
			login(request, user)
			messages.success(request, 'You Have Successfully Registered! Welcome...')
			return redirect('saludo')
	else:
		form = SignUpForm()

	context={'form':form}

	return render(request,'register.html',context)

'''La funcion COSTUMER_RECORD usa pk como parametro para solicitar el 
	id del objeto que queremos visualizar en la BD, luego devuelve el
	objeto
'''
def costumer_record(request,pk):
	if request.user.is_authenticated:
		#See the records
		costumer_record = Record.objects.get(id=pk)
		return render(request,'record.html',{'costumer_record':costumer_record})
	else:
		messages.error(request, 'You Must Be Authenticated To Access Here!...')
		return redirect('saludo')

def delete_record(request,pk):
	if request.user.is_authenticated:
		#Delete the records
		erase_record = Record.objects.get(id=pk)
		erase_record.delete()
		messages.success(request, 'Record deleted Successfully!...')
		return redirect('json')
	else:
		messages.error(request, 'You Must Be Authenticated To Access Here!...')
		return redirect('saludo')
	''' 
	La funcion CREATE_RECORD es la que salva registros en la BD. Crea una una instancia 
	del formulario CREATE_RECORD_FORM valida si el metodo es POST, luego salva la instancia
	del formulario con FORM.SAVE(). 
	'''
def create_record(request):
	form = CreateRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('json')
		return render(request, 'create_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('saludo')
	'''
	La funcion UPDATE_RECORD usa pk como parametro para solicitar el 
	id del objeto que queremos modificar en la BD, luego crea una instancia del objeto
	 CREATE_RECORD_FORM y le pasa el ID luego valida si la forma es valida y la salva
	'''
def update_record(request,pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = CreateRecordForm(request.POST or None, instance = current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Updated Successfully...")
			return redirect('json')
		return render(request, 'update_record.html', {'form':form,'current_record':current_record})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('saludo')