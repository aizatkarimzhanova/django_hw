from django.urls import path
from . import views

urlpatterns = [
    path("citation/", views.citation_view),
    path("book_list/", views.book_list),
    path("book_list/<int:id>/",views.book_detail),
]