from django.shortcuts import render

# Create your views here.

def firstview(request):
    return render(request,"html/first.html")

def secondview(request):
    return render(request,"html/second.html")
