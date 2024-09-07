# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

#from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import UserCreationForm

#def login_view(request):
#    if request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#            login(request, user)
#            return redirect('home')
#        else:
#            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
#    return render(request, 'accounts/login.html')

#def logout_view(request):
#    logout(request)
#    return redirect('login')

#def register_view(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('login')
#    else:
#        form = UserCreationForm()
#    return render(request, 'accounts/register.html', {'form': form})
