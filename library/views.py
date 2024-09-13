from django.shortcuts import render, redirect
from . forms import SignupForm

# Create your views here.

def register(request):
    return render(request, 'register.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = SignupForm 
        return render(request, 'signup.html', {'form':form})


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')



def create(request):
    return render(request, 'create.html')