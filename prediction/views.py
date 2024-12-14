from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    template=loader.get.template("home.html")
    res=template.render()
    return HttpResponse(res)


# Create your views here.
