from django.urls import path
from . import views


urlpatterns = [
    path('registrations/', views.RegistrationListView.as_view()),
    path('persons/', views.PersonListView.as_view()),
    path('tours/', views.TourListView.as_view()),
    path('registrations/', views.RegistrationListView.as_view()),
    path('reviews/', views.ReviewListView.as_view()),
    
    
]
