from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name').split(' ')

            user = User.objects.get(username=username)
            user.email = username
            user.first_name = name[0]
            user.last_name = name[1]
            user.save()
            messages.success(request, f'Account is created for {username}')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})
