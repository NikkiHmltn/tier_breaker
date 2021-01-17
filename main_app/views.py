from django.shortcuts import render
from .models import Bracket
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

############## USER ###################    

def login_view(request):
  #ifpost then auth the user
  if request.method == 'POST': 
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      u = form.cleaned_data['username']
      p = form.cleaned_data.get('password')
      user = authenticate(username=u, password=p)
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/user/' + u)
        else: 
          print(f'The account for {u} has been disabled.')
      else: 
        print(f'The username and/or password is incorrect.')
    else:
      form = AuthenticationForm()
      return render(request, 'login.html', {'form': form})
  else: # get reuqest that send up an empty form
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/')

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return HttpResponseRedirect('/user/' + str(user))
    else: 
      form = UserCreationForm()
      return render(request, 'signup.html', {'form': form})
  else:
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})