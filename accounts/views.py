from django.shortcuts import render , redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'accounts/home.html')



def register(request):
    if request.method=='GET':
        form = RegistrationForm()
        args = {'form': form}
        return render(request , 'accounts/register.html' , args)
    else:
        form= RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')

@login_required
def profile(request):
    args = {'user': request.user}
    return render(request , 'accounts/profile.html', args)


