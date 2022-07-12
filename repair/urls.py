from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', show_about, name='about'),
    path('<slug:cat_slug>/', show_category, name='category'),
    path('<slug:cat_slug>/<slug:serv_slug>/', show_service, name='service'),
]
