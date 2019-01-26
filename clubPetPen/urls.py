from django.urls import path
from . import views

app_name='clubPetPen'
urlpatterns = [
    path('', views.idk, name='login'),
    #path('', views.loginView.as_view(), name='login'),
    ]