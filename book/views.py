from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def citation_view(request):
    if request.method == "GET":
        return HttpResponse("Влюбиться можно в красоту, но полюбить – лишь только душу!(Шекспир)")

def book_detail(request, id):
    if request.method == "GET":
        book_id = get_object_or_404(models.Book, id=id)
        return render(
            request,
            "book_details.html",
            {
               "book_detail": book_id
            }
        )    
    
def book_list(request):
    if request.method == "GET":
        book_list = models.Book.objects.all()
        return render(
            request,
            "book_list.html",
            {
                "book_list": book_list
            }
        )
    
