# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import random
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import  urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


from carts.views import _cart_id
from carts.models import Cart, CartItem
from .models import Account
from .forms import RegistrationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            email_prefix = email.split("@")[0] # ================Extract email prefix
# =========Randomly select three digits from the phone number
            last_three_digits = ''.join(random.sample(phone_number, 3))
# Combine email prefix and last three digits of phone number
            username = f"{email_prefix}{last_three_digits}"

            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name,
                email=email, username=username, password=password
                )
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration successful.')
            return redirect('register')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return 