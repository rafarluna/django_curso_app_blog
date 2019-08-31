from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class SignupView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        form = SignupForm()
        return render(request, 'signup.html', locals())

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create(username=username, is_active=True)
            user.set_password(password)
            user.save()
            login(request, user) #, backend="django.contrib.auth.backends.ModelBackend")
            return redirect('/')
        return render(request, 'signup.html', locals())


class LoginView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        form = LoginForm()
        return render(request, 'login.html', locals())

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            login(request, user) #, backend="django.contrib.auth.backends.ModelBackend")
            return redirect('/')
        return render(request, 'login.html', locals())
