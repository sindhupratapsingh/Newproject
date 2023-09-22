from django.contrib import admin
from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('user_data/', views.user_data, name='user_data'),
    



]