from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def HomePage(req):
    # return HttpResponse('<h1>Hello World</h1>')
    return render(req, 'school/home.html')
