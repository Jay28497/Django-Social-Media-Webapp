from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages
import random
from .models import UserOTP
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def signup(request):
    if request.method == "POST":
        get_otp = request.POST.get('otp')
        if get_otp:
            get_user = request.POST.get('user')
            user = User.objects.get(username=get_user)
            if int(get_otp) == UserOTP.objects.filter(user=user).last().otp:
                # user activate true
                user.is_active = True
                user.save()

                messages.success(request, f'Account is created for {user.username}')
                return redirect('login')
            else:
                messages.warning(request, f'You have entered a wrong OTP. Please enter the correct OTP.')
                return render(request, 'user/signup.html', {'otp': True, 'user': user})

        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name').split(' ')

            user = User.objects.get(username=username)
            user.email = username
            user.first_name = name[0]
            user.last_name = name[1]

            # user activate false
            user.is_active = False
            user.save()

            # OTP generate
            user_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=user, otp=user_otp)

            mess = f"Hello {user.first_name}, \nYour OTP is {user_otp} \nThanks !!"

            # Email subject and body
            send_mail(
                "Welcome to Social Media Website - Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False
            )

            return render(request, 'user/signup.html', {'otp': True, 'user': user})
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


def resend_otp(request):
    if request.method == "GET":
        get_user = request.GET['usr']
        if User.objects.filter(username=get_user).exists() and not User.objects.get(username=get_user).is_active:
            user = User.objects.get(username=get_user)

            # OTP generate
            user_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=user, otp=user_otp)

            mess = f"Hello {user.first_name}, \nYour OTP is {user_otp} \nThanks !!"

            # Email subject and body
            send_mail(
                "Welcome to Social Media Website - Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False
            )

            return HttpResponse("Resend ")
    return HttpResponse("Can't send ")
