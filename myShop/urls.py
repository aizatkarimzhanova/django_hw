from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categories_view, name='categories'),  # /categories/
    path('products/', views.products_view, name='products'),        # /products/
    path('category/<int:category_id>/', views.category_products_view, name='category_products'),  # /category/1/
]


