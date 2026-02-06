from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="название книги")
    author = models.CharField(max_length=150, verbose_name="автор") 
    genre = models.CharField(max_length=150, verbose_name="жанр книги")              
    description = models.TextField(verbose_name="описание")      
    pages = models.PositiveIntegerField(verbose_name="количество страниц") 
    cover = models.ImageField(upload_to='covers/', verbose_name="обложка")  
    file = models.FileField(upload_to='books/', null=True, blank=True)     # файл книги (pdf и т.д.)
    language = models.CharField(max_length=50, verbose_name="язык")              
    rating = models.FloatField(verbose_name="рейтинг")      
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"

