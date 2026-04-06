from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
