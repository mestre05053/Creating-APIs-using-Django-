from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm, CreateRecordForm
from .models import Record

###API imports
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecordSerializer

#Json imports
from django.http import JsonResponse
import json
from django.core.serializers import serialize



#Api Serializers Class

class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Record.objects.all().order_by('created_at')
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticated]

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

def records(request):
	if request.user.is_authenticated:
		records = Record.objects.all().order_by('-created_at')
		context = {'records':records}
		return render(request, 'records.html', context)
	else:
		messages.error(request, 'You Must Be Authenticated To Access Here!...')
		return redirect('saludo')

def data_json(request):
	data = list(Record.objects.values())
	print(data)
	return JsonResponse(data, safe=False)

def json_model(request):
	return render(request, 'json_data.html', {'data':data})
	
	'''
	data = list(Record.objects.values())
	json_data = list(JsonResponse(data, safe=False))
	print(json_data)
	context = {'json_data':json_data}
	return render(request, 'json_data.html', context)
	'''
	'''
	qs = Record.objects.all()
	data = serialize("json", qs, fields=('first_name', 'last_name'))
	context = {'data':data}
	print(data)
	return render(request, 'json_data.html', context)
	'''

def logout_user(request):
	logout(request)
	messages.success(request,'You Have Logged Out...')
	return redirect('saludo')

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
		return redirect('records')
	else:
		messages.error(request, 'You Must Be Authenticated To Access Here!...')
		return redirect('saludo')

def create_record(request):
	form = CreateRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('records')
		return render(request, 'create_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('saludo')


def update_record(request,pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = CreateRecordForm(request.POST or None, instance = current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Updated Successfully...")
			return redirect('records')
		return render(request, 'update_record.html', {'form':form,'current_record':current_record})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('saludo')