from django.shortcuts import render
from .models import Cricketer
# Create your views here.

def home(request):
    cricketers_list=Cricketer.objects.all()
    data={
        "cricketers":cricketers_list,
    }
    return render(request,"home.html",data)

