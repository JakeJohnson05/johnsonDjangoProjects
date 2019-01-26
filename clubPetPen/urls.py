from django.urls import path, include
from . import views
from django.contrib import admin

app_name='clubPetPen'
urlpatterns = [
    path('', views.idk, name='placeholder'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('', views.loginView.as_view(), name='login'),
    ]
