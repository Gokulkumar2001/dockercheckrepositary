from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('login_submission/',views.login_submission,name='login_submission')
]