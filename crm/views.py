from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm, CreateRecordForm
from .models import Record

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
		return redirect('json')
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
				return redirect('json')
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
			return redirect('json')
		return render(request, 'update_record.html', {'form':form,'current_record':current_record})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('saludo')