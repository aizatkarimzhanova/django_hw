from django.urls import path
from . import views

urlpatterns = [
    path("citation/", views.citation_view),
]