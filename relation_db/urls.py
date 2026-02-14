from django.urls import path
from . import views

urlpatterns = [
    path("people/", views.person_list, name="person_list"),
    path("tours/", views.tour_list, name="tour_list"),
    path("categories/", views.category_list, name="category_list"),
]

