from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.core.mail import send_mail

from .forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        next_page = request.GET.get('next_page', '')
        return render(request, 'user/register.html', context={'register_form': register_form, 'next_page': next_page})

    def post(self, request):
        next_page = request.POST.get('next_page', '')
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Subject here',
                'Here is the message.',
                'user_admin@email.com',
                [form.email],
                fail_silently=False,
            )
            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(reverse('home'))
        else:
            register_form = RegisterForm()
            return render(request, 'user/register.html', context={'register_form': register_form})
