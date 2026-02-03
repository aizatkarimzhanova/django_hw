from django.shortcuts import render
from django.http import HttpResponse

def citation_view(request):
    if request.method == "GET":
        return HttpResponse("Влюбиться можно в красоту, но полюбить – лишь только душу!(Шекспир)")
    
