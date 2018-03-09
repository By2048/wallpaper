from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.urls import reverse

from . import forms


# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = forms.RegisterForm()
        return render(request, 'user/register.html', context={'form': form})

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = forms.RegisterForm()
            return render(request, 'user/register.html', context={'form': form})


class LoginView(View):
    def get(self,request):
        pass
    def pose(self,request):
        pass


class ChangePassword(View):
    def get(self,request):
        pass
    def post(self,request):
        pass

class ResetPassword(View):
    def get(self,request):
        pass
    def post(self,request):
        pass



