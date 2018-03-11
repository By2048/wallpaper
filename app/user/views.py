from django.shortcuts import render, redirect
from django.views.generic.base import View

from . import forms


class RegisterView(View):
    def get(self, request):
        form = forms.RegisterForm()
        next = request.GET.get('next', '')
        return render(request, 'user/register.html', context={'form': form, 'next': next})

    def post(self, request):
        next = request.POST.get('next', '')
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            if next:
                return redirect(next)
            else:
                return redirect(reversed('index'))
                # return redirect('index')
        else:
            form = forms.RegisterForm()
            return render(request, 'user/register.html', context={'form': form})



class ChangePassword(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class ResetPassword(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
