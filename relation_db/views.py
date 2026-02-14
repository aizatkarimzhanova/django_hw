
from django.shortcuts import render
from . models import Person, Tour, Category

def person_list(request):
    people = Person.objects.all()
    return render(
        request, 
        "relation_db/person_list.html",
        {
            "people": people
            }
        )

def tour_list(request):
    tours = Tour.objects.all()
    return render(
        request,
        "relation_db/tour_list.html",
        {
            "tours": tours
            }
        )

def category_list(request):
    categories = Category.objects.all()
    return render(
        request,
        "relation_db/category_list.html",
        {
            "categories": categories
            }
            )

