from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from pprint import pprint
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator

class LoginView(View):
    def get(self, request):
        return render(request, 'osso/index.html', { 'form': UserCreationForm() })

class ProfileView(View):
    @method_decorator(login_required)
    def get(self, request):
        print("{}".format(request.user.is_authenticated))
        pprint(request.user.social_auth)
        return render(request, 'osso/profile.html')