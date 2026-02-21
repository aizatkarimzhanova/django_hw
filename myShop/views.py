from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic



class AllCategoriesView(generic.ListView):
    template_name = 'categories.html'
    context_object_name = 'categories'
    model = models.Category



#def all_categories(request):
#    categories = models.Category.objects.all()
#    return render(
#            request,
#            'categories.html',
#            {
#                    "categories": categories
#            }
#        )



class AllProductsView(generic.ListView):
    template_name = 'products.html'
    context_object_name = 'products'
    model = models.Product



#def all_products(request):
#    products = models.Product.objects.all()
#    return render(
#            request,
#            'products.html',
#            {
#                    "products": products
#            }
#        )



class CategoryProductsView(generic.ListView):
    template_name = 'category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(models.Category, id=self.kwargs['id'])
        return self.category.products.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context



#def category_products(request, id):
#    category = get_object_or_404(models.Category, id=id)
#    products = category.products.all()
#    return render(
#            request,
#            'category_products.html',
#            {            
#                    "products": products,
#                    "category": category     
#            }
#        )
