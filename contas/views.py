from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def home(request):
    data={}
    data['now'] = datetime.datetime.now()
    #html= f"<html><body> agora é {now}.</body><html>"
    return render(request, 'contas/home.html',data)