from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models
from .forms import BookForm
from .models import Book
from django.core.paginator import Paginator

def books_list(request):
    query = request.GET.get("q")  
    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    paginator = Paginator(books, 4)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "books_list.html", {
        "page_obj": page_obj,
        "q": query
    })

def citation_view(request):
    return HttpResponse("Влюбиться можно в красоту, но полюбить – лишь только душу! (Шекспир)")


# READ: список книг
def book_list(request):
    query = request.GET.get('q')
    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    paginator = Paginator(books, 5)  # 5 книг на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'book_list.html', {
        'page_obj': page_obj
    })


# READ: детали книги
def book_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(
        request,
        "book_details.html",
        {
            "book_detail": book
        }
    )


# CREATE: создать книгу
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(
        request,
        "book_form.html",
        {
            "form": form
        }
    )


# UPDATE: обновить книгу
def book_update(request, id):
    book = get_object_or_404(models.Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(
        request,
        "book_form.html",
        {
            "form": form
        }
    )


# DELETE: удалить книгу
def book_delete(request, id):
    book = get_object_or_404(models.Book, id=id)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(
        request,
        "book_confirm_delete.html",
        {
            "book": book
        }
    )

