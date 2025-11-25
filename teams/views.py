from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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


def home(request):
    return HttpResponse("<h1>Witaj na stronie glownej aplikacji</h1><p><a href='/login/'>Zaloguj sie</a> lub <a href='/teams/register/'>Zarejestruj</a></p>")






@login_required
def profile(request):
    return render(request, 'teams/profile.html')


