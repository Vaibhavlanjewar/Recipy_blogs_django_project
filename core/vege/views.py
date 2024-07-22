from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

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