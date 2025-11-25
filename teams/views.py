from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import UserProfile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            UserProfile.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city']
            )
            return redirect('login')  # tymczasowo – jeszcze nie mamy strony logowania
    else:
        form = UserRegistrationForm()
    return render(request, 'teams/register.html', {'form': form})


