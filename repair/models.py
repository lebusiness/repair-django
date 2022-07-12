from django.db import models
from django.urls import reverse

# Create your models here.

# Главный
class Chief(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Имя")
    number = models.CharField(max_length=100, verbose_name="Номер")
    experience = models.IntegerField(verbose_name="Стаж")

    def __str__(self):
        return self.name   

    class Meta:
        verbose_name = 'Главный'
        verbose_name_plural = 'Главный'
        ordering = ['id']

# Бригада
class Brigade(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    worker_count = models.IntegerField(verbose_name="Количество рабочих")
    hour_price = models.IntegerField(verbose_name="Цена за час")

    chief = models.ForeignKey('Chief', on_delete=models.PROTECT, verbose_name="Главный")

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Бригада'
        verbose_name_plural = 'Бригада'
        ordering = ['id']

# Категория
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    descr = models.TextField(blank=True, verbose_name="Описание")
    img = models.ImageField(upload_to="photos/caregories", verbose_name="Фото")

    brigade = models.ForeignKey('Brigade', on_delete=models.PROTECT, verbose_name="Бригада")

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

# Отзывы
class Feedback(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Имя")
    text = models.TextField(blank=True, verbose_name="Отзыв")

    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
        ordering = ['id']

# Портфолио
class Portfolio(models.Model):
    img = models.ImageField(upload_to="photos/portfolio/", verbose_name="Фото")

    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        ordering = ['id']

# Услуга
class Service(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    descr = models.TextField(blank=True, verbose_name="Описание")
    img = models.ImageField(upload_to="photos/services/", verbose_name="Фото")
    hours = models.IntegerField(verbose_name="Часы Работы")
    price = models.IntegerField(verbose_name="Цена")

    # brigade = models.ForeignKey('Brigade', on_delete=models.PROTECT, verbose_name="Бригада")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    # def get_absolute_url(self):
    #     return reverse('cat_slug', kwargs={'serv_slug': self.slug})

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуга'
        ordering = ['id']

