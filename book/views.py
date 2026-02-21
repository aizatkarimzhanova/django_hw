from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models, forms
from django.core.paginator import Paginator
from django.db.models import F
from django.views import generic



class SeachView(generic.ListView):
     template_name = 'book_list.html'
     context_object_name = 'book_list'
     model = models.Book

     def get_queryset(self):
          return self.model.objects.filter(title__icontains=self.request.GET.get('oleg'))
     
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['oleg'] = self.request.GET.get('oleg')
          return context


#def search_view(request):
#    query = request.GET.get("oleg", '')
#    if query:
#       book_list = models.BookList.objects.filter(title__icontains=query)
#    else:
#        book_list 
#        book_list = models
#        book_list = models= models.BookList.objects.none
#    
#    return render(
#        request,
#        'book_list.html',
#        {
#            "book_list": book_list
#        }
#
#    )



class UpdateBookListView(generic.UpdateView):
     template_name = 'update_book.html'
     form_class = forms.BookForm
     model = models.Book
     success_url = '/book_list/'

     def get_object(self, **kwargs):
          book_id = self.kwargs.get('id')
          return get_object_or_404(self.model, id=book_id)
     
     def form_valid(self, form):
          print(form.changed_data)
          return super(UpdateBookListView, self).form_valid(form=form)




#def update_book_view(request, id):
#     book_id = get_object_or_404(models.BookList, id=id)
#     if request.method == "POST":
#          form = forms.BookListForm(request.POST, instance=book_id)
#          if form.is_valid():
#               form.save()
#               return redirect('/book_list/')
#     else:
#          form = forms.BookListForm(instance=book_id)
#     return render(
#          request,
#          'update_book.html',
#          {
#               "form": form,
#               "book_id": book_id
#          }
#     )




class DeleteBookListView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/book_list/'
    context_object_name = 'book_detail_id'
    model = models.Book

    def get_object(self, **kwargs):
          book_id = self.kwargs.get('id')
          return get_object_or_404(self.model, id=book_id)



#def delete_book_view(request, id):
#     book_id = get_object_or_404(models.BookList, id=id)
#     book_id.delete()
#     return redirect('/book_list/')



class CreateBookListView(generic.CreateView):
    template_name = 'create_book.html'
    form_class = forms.BookForm
    success_url = '/book_list/'


    def form_valid(self, form):
        print(form.changed_data)
        return super(CreateBookListView, self).form_valid(form=form)


#def create_book_view(request):
#    if request.method == 'POST':
#        form = forms.BookListForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('/book_list/')
#    else:
#            form = forms.BookListForm()
#    return render(
#         request,
#         'create_book.html',
#         {
#              "form": form
#         }
#    )



class BookListDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'
    pk_url_kwarg = 'id'
    model = models.Book

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request

        views_book = request.session.get('viewed_book', [])

        if obj.pk not in views_book:
            models. Book.objects.filter(pk=obj.pk).update(
                views = F("views")+1
            )
            views_book.append(obj.pk)
            request.session['viewed_book'] = views_book

            obj.refresh_from_db()
        return obj


#def book_detail_view(request, id):
#    if request.method == 'GET':
#        book_detail_id = get_object_or_404(models.BookList, id=id)
#        views_book = request.session.get('viewed_book', [])
#        
#        if id not in views_book:
#
#            book_detail_id.views = F("views") + 1
#            book_detail_id.save()
#            book_detail_id.refresh_from_db()
#
#            views_book.append(id)
#            request.session['viewed_book'] = views_book
#
#
#        return render(
#            request,
#            'book_detail.html',
#            {
#                "book_id": book_detail_id
#            }
#        )



class BookListListView(generic.ListView):
    template_name = 'book_list.html'
    model = models.Book
    context_object_name = 'book_list'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['book_list'] = context['page_obj']
        return context



#def book_list_view(request):
#    if request.method == 'GET':
#        book_list = models.BookList.objects.all()
#        paginator = Paginator(book_list, 2)
#        page = request.GET.get("page")
#        page_obj = paginator.get_page(page)
#        return render(
#            request,
#            'book_list.html',
#            {
#                    "book_list": page_obj
#            }
#        )
    



def quotes_view(request):
    if request.method == 'GET':
        return HttpResponse("Люди приходят и уходят!")


