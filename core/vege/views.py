from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# to save the data got from frontend to backend import model Recipy
from .models import Recipy
# Create your views here.

# routs 
def recipies(request):
    if request.method=="POST":
      data=request.POST
      
      recipy_name=data.get('recipy_name')
      recipy_description=data.get('recipy_description')
      recipy_image=request.FILES['recipy_image']

      print(recipy_name)
      print(recipy_description)
      print(recipy_image)
      
    #   create record 
      Recipy.objects.create(
                          recipy_name=recipy_name,
                          recipy_description=recipy_description,
                          recipy_image=recipy_image,
                          )
      return redirect('/recipies/')
      
    queryset=Recipy.objects.all()  
    context={'recipies':queryset}  # to show the backend data on frontend by using context 
    return render(request,'recipies.html',context)


def viewRecipies(request):
   queryset=Recipy.objects.all()
   context={'recipies':queryset}
   return render(request,'viewRecipies.html',context)

 
def delete_recipy(request,id):
   queryset=Recipy.objects.all()
   queryset.filter(id=id).delete()
   return redirect('/recipies/')


def login_page(request):
  if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')

      if not User.objects.filter(username=username).exists():
         messages.error(request,"Invalid username")
      user=authenticate(username=username,password=password) 

      if user is None:   
         messages.error(request,"Invalid password")
         return redirect('/login_page/')
      else:
        login(request,user)
        return redirect('/recipies/')
         
  return render(request,'login.html')

def logout_page(request):
  logout(request)
  return redirect('/login_page/')
  
    
  
  




def register_page(request):
   if request.method=='POST':
      first_name=request.POST.get('first_name')
      last_name=request.POST.get('last_name')
      username=request.POST.get('username')
      password=request.POST.get('password')


      user=User.objects.filter(username=username)
      if user.exists():
         messages.info(request,'username already taken')
         return redirect('/register_page/')

      user=User.objects.create(
         first_name=first_name,
         last_name=last_name,
         username=username,
      )
      user.set_password(password) #password can be encrypted by this 
      user.save()
      return redirect('/register_page/')
      messages.info(request,'Accouunt created successfully')

   return render(request,'register.html')
