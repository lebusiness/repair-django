from unicodedata import category
from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, 'repair/index.html', {'categories': categories})

def show_category(request, cat_slug):
    categories = Category.objects.all()

    category = categories.filter(slug = cat_slug).last()
    category_title = category.name
    category_descr = category.descr
    category_id = category.pk
    category_brigade = category.brigade_id

    services = Service.objects.filter(id = category_brigade)

    brigade = Brigade.objects.all().filter(id = category_id).last()
    brigade_title = brigade.name
    brigade_count = brigade.worker_count
    brigade_price = brigade.hour_price
    brigade_chief = brigade.chief_id

    chief = Chief.objects.all().filter(id = brigade_chief).last()
    chief_name = chief.name
    chief_number = chief.number
    chief_experience = chief.experience

    portfolioImgs = Portfolio.objects.all().filter(category = category_id)
    feedbacks = Feedback.objects.all().filter(category = category_id)

    return render(request, 'repair/category.html', {
        
        'categories': categories, 
        'category': category,
        'category_title': category_title, 
        'category_descr': category_descr, 

        'services': services,

        'brigade_title': brigade_title,
        'brigade_count': brigade_count,
        'brigade_price': brigade_price,

        'chief_name': chief_name,
        'chief_number': chief_number,
        'chief_experience': chief_experience,

        'portfolioImgs': portfolioImgs,

        'feedbacks' : feedbacks,
    })

def show_service(request, serv_slug, *args, **kwargs):
    categories = Category.objects.all()

    services = Service.objects.all()
    service = services.filter(slug = serv_slug).last()

    service_title = service.name
    service_descr = service.descr
    service_time = service.hours
    service_price = service.price
    service_img = service.img
    category_title = service.category.name
    
    return render(request, 'repair/service.html', {
        'categories': categories, 
        'category_title': category_title,
        'title': service_title, 
        'descr': service_descr, 
        'time': service_time,
        'price': service_price,
        'service_img': service_img,
    })

def show_about(request):
    categories = Category.objects.all()

    return render(request, 'repair/about.html', {
        'categories': categories, 
    })