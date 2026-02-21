from django.views import generic
from . import models


class CategoryListView(generic.ListView):
    template_name = 'category_list.html'
    context_object_name = 'categories'
    model = models.Category



class PersonListView(generic.ListView):
    template_name = 'person_list.html'
    context_object_name = 'persons'
    model = models.Person



class TourListView(generic.ListView):
    template_name = 'tour_list.html'
    context_object_name = 'tours'
    model = models.Tour


class RegistrationListView(generic.ListView):
    template_name = 'registration_list.html'
    context_object_name = 'registrations'
    model = models.Registration


class ReviewListView(generic.ListView):
    template_name = 'review_list.html'
    context_object_name = 'reviews'
    model = models.Review
