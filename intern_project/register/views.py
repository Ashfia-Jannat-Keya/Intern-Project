from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.

def index(request):
	return render(request, 'index.html')

def register(request):
	if request.method =="POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		if User.objects.filter(username=username).exists():
			messages.info(request, "Username already exists!")
		else:
			if User.objects.filter(username=email).exists():
				messages.info(request, "Email already exists!")
			else:
				return redirect('registerinfo')
				
				
					
	return render(request, 'register.html', {'messages':messages})

def login(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		auth_login(request,user)
		return redirect('info')
	return render(request, 'login.html')

def info(request):
	return render(request, 'info.html')

def registerinfo(request):
	if request.method =="POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		data = User.objects.create_user(username=username, password=password,email=email, first_name=firstname, last_name=lastname)
		data.save()
		messages.success(request, "User created successfully!")
		user = authenticate(username=username,password=password)
		auth_login(request,user)
		return redirect('/')
	return render(request, 'registerinfo.html')

