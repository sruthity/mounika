from django.shortcuts import render,HttpResponse
from app_1.models import *

def mouni(request):
    a=sruthi_1.objects.all()
    for i in a:
        r=i.input11
    b=sruthi_2.objects.all()
    if sruthi_2.objects.filter():
        c=sruthi_2(input2=18,input3=12)
        c.save()
    for i in b:
        u=i.input2
    return HttpResponse('hello world'+r+u+" ")

# Create your views here.
