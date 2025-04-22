from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import SingUpForm


User = get_user_model()

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('movies:home')
    else:
        return render(request, 'signup.html', context={'form': SingUpForm()})