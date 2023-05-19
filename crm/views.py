from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm
from .models import Record

def saludo(request):
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

def json(request):
	records = Record.objects.all()
	context = {'records':records}

	return render(request, 'json.html', context)

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
