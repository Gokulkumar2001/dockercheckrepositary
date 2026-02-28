from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from sampleapp.models import Login


# Create your views here.



def index(request):
    # return HttpResponse("Success")
    return render(request,'index.html',{"msg":"Welcome to My Page"})

def login_submission(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_login = Login.objects.filter(name=username,password=password)
        if len(check_login) >0 :
            return render(request, 'welcome.html', {"msg": "Welcome to My Sample Project"})
        else:
            messages.error(request,'please cheack your username or password',extra_tags='failed')
            return render(request, 'index.html', {"msg": "User Not Registered"})
    # return HttpResponse("Success")
