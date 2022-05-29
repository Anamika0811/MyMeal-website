from django.urls import path
from app import views


urlpatterns = [
    path('',views.Index, name='Index'),
    path('login.html',views.Login, name ='Login'),
    # path('profile.html',views.output, name ='script'),
]
