from django.urls import path
from . import views
app_name='book'

urlpatterns = [
    path('quotes/', views.quotes_view),
    path('book_list/', views.BookListListView.as_view(), name='knizhnyi_pir'),
    path('book_list/<int:id>/', views.BookListDetailView.as_view(), name='knizhnoe_menu'),
    path('book_list/<int:id>/delete', views.DeleteBookListView.as_view(), name='kniga_terminator'),
    path('book_list/<int:id>/update', views.UpdateBookListView.as_view(), name='peresolit_knigu'),
    path('create_book_list/', views.CreateBookListView.as_view(), name='sozdat_blog'),
    path('search/', views.SeachView.as_view(), name='iskat_recepty'),
    

]