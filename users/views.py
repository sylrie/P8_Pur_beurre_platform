""" Views for users app """

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from product.models import FavoriteProduct


def register(request):
    title = "Inscription"
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Ton compte a bien été créé, tu peux te connecter.')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {'form': form, 'title': title})

def login(request, message=None):
    if message:
        return render(request,'users/login.html', {'message': message})
    else:
        return render(request,'users/login.html')     

@login_required
def logout(request):

    return render(request,'users/logout.html', {'title': "Déconnexion"})

@login_required
def profile(request):
    name = str(request.user).capitalize()
    favorites = len(FavoriteProduct.objects.filter(user=request.user))
    return render(request, 'users/profile.html', {'title': "Profil", 'name': name, 'favorites': favorites})