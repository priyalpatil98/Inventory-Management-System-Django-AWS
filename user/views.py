from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from dashboard import order_sns
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
#            email_id = form.cleaned_data.get('email')
            form.save()
            messages.success(request, f'Account has been created for { username } Successfully! Please Continue to Log in')
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form' : form,
    }
    return render(request, 'user/register.html', context)

def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Profile updated Successfully!') #Flash Message
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context={
        'user_form' : user_form,
        'profile_form' : profile_form,
    }
    return render(request, 'user/profile_update.html', context)