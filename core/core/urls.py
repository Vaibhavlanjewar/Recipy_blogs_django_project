# core/urls.py
from django.contrib import admin
from django.urls import path, include
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('', recipies, name='home'),  # Set recipies as the home page
    # path('home/', home, name='home'),  # Rename the previous home path to /home/
    path('recipies/', recipies, name='recipies'),
  
    path('viewRecipies/', viewRecipies, name='viewRecipies'),
    path('delete_recipy/<id>', delete_recipy, name='delete_recipy'),
    path('login_page/',login_page,name='login_page'),
    path('register_page/',register_page,name='logout_page'),
    path('logout_page/',logout_page,name='register_page'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
