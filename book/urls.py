from django.urls import path
from . import views

urlpatterns = [
    path("citation/", views.citation_view, name="citation"),

    # READ
    path("books/", views.book_list, name="book_list"),
    path("books/<int:id>/", views.book_detail, name="book_detail"),

    # CREATE
    path("books/create/", views.book_create, name="book_create"),

    # UPDATE
    path("books/<int:id>/update/", views.book_update, name="book_update"),

    # DELETE
    path("books/<int:id>/delete/", views.book_delete, name="book_delete"),
]
