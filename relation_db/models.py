from django.db import models

#  Модель человека
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    
    # 1 человек → 1 тур (тур может иметь много людей)
    tour = models.ForeignKey(
        'Tour',
        on_delete=models.SET_NULL,
        related_name='people',
        null=True,
        blank=True
    )

    # Many-to-many: категории туристов
    categories = models.ManyToManyField('Category', related_name='people', blank=True)

    def __str__(self):
        return self.name


# Тур (4 вида через choices)
class Tour(models.Model):
    TOURS = (
        ("horse", "Конный тур"),
        ("mountain", "Горный тур"),
        ("lake", "Тур на озеро"),
        ("city", "Городской тур"),
    )
    name = models.CharField(max_length=50, choices=TOURS, default="horse")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Отзывы о человеке (1:many)
class Review(models.Model):
    MARKS = (
        ("1", "1 – очень плохо"),
        ("2", "2 – плохо"),
        ("3", "3 – нормально"),
        ("4", "4 – хорошо"),
        ("5", "5 – очень хорошо"),
    )

    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='reviews')
    mark = models.CharField(max_length=1, choices=MARKS)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person.name} - {self.mark}"


#Категории туристов (many-to-many)
class Category(models.Model):
    name = models.CharField(max_length=50)  # например: школьник, взрослый, пенсионер

    def __str__(self):
        return self.name
