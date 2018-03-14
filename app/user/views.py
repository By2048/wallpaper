from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

from . import forms


# class RegisterView(View):
#     def get(self, request):
#         form = forms.RegisterForm()
#         next_page = request.GET.get('next', '')
#         return render(request, 'user/register.html', context={'form': form, 'next': next_page})
#
#     def post(self, request):
#         next_page = request.POST.get('next', '')
#         form = forms.RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             if next_page:
#                 return HttpResponseRedirect(reverse(next_page))
#             else:
#                 return HttpResponseRedirect(reverse('index'))
#         else:
#             form = forms.RegisterForm()
#             return render(request, 'user/register.html', context={'form': form})
