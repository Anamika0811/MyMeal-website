from django.shortcuts import render
from django.http import HttpResponse





def Index(request):
    return render(request,'app/index.html')

def Login(request):
    return render(request, 'app/login.html')

# def unsuccessful(request):
#     return render(request, 'app/index.html')

# def output(request):
#     return render(request, 'profile.html')