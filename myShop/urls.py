from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.AllCategoriesView.as_view()),
    path('products/', views.AllProductsView.as_view()),
    path('category/<int:id>/', views.CategoryProductsView.as_view())
    
]


