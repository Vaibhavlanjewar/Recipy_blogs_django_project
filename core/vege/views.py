from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Recipy
from django.contrib.auth import authenticate,login,logout
from django.contrib.messages import constants as messages
from django.contrib.auth.decorators import login_required

from django.contrib import messages

@login_required(login_url='/login_page/')
def recipies(request):
    if request.method == "POST":
        data = request.POST
        recipy_name = data.get('recipy_name')
        recipy_description = data.get('recipy_description')
        recipy_image = request.FILES.get('recipy_image')

        Recipy.objects.create(
            recipy_name=recipy_name,
            recipy_description=recipy_description,
            recipy_image=recipy_image,
        )
        return redirect('/recipies/')

    queryset = Recipy.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipy_name__icontains=request.GET.get('search'))

    context = {'recipies': queryset}
    return render(request, 'recipies.html', context)

def viewRecipies(request):
    queryset = Recipy.objects.all()
    context = {'recipies': queryset}
    return render(request, 'viewRecipies.html', context)

def delete_recipy(request, id):
    Recipy.objects.filter(id=id).delete()
    return redirect('/recipies/')

def update_recipies(request, id):
    recipy = Recipy.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        recipy_name = data.get('recipy_name')
        recipy_description = data.get('recipy_description')
        recipy_image = request.FILES.get('recipy_image')

        recipy.recipy_name = recipy_name
        recipy.recipy_description = recipy_description
        if recipy_image:
            recipy.recipy_image = recipy_image

        recipy.save()
        return redirect('/recipies/')

    context = {'recipy': recipy}
    return render(request, 'update_recipies.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('/login_page/')

        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid password')   
        else:
            # seesion
            login(request,user)  
            return redirect('/recipies/')   
        
    return render(request, 'login_page.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already taken ')
            return redirect('/register/')
       
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()

        messages.info(request,'Account created sucessFully ')

    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login_page/')
