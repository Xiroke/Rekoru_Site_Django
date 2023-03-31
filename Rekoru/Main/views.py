from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

def Index(request):
	return render(request, 'Main/index.html')


def Catalog(request):
	return render(request, 'Main/catalog.html')


def Accounts(request):
	return render(request, 'Main/accounts.html')

def Registration(request):
	# Проверка что есть запрос POST
	if request.method == 'POST':
		# Создаём форму
		form = UserRegistrationForm(request.POST)
		# Валидация данных из формы
		if form.is_valid():
			# Сохраняем пользователя
			form.save()
			# Рендаринг страницы
			return redirect('IndexUrl')
	else: # Иначе
		# Создаём форму
		form = UserRegistrationForm()
		# Передаём форму для рендеринга
		# Рендаринг страницы
	return render(request, 'Main/registration.html', {'form': form})

def Login(request): 
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = AuthenticationForm(request=request,data=request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request,user)
					messages.success(request,'Logged in successfully!!!')
					return redirect('AccountsUrl')
		else:
			form = AuthenticationForm()
		return render(request,'Main/login.html',{'form':form})
	else:
		return redirect('AccountsUrl')
	
def Logout(request):
	logout(request)
	return redirect('AccountsUrl')


def Addproject(request):
# 	if request.method == 'POST':

# 		if form.is_valid()

# 			return redirect('AccountsUrl')
# 	else:
# 		form = AddprojectForm()
	return render(request, 'Main/addproject.html')