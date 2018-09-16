from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('/posts')

	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form' : form})

@login_required(login_url="/accounts/login/")
def logout_view(request):
	auth.logout(request)
	return render(request, 'accounts/logout.html')
