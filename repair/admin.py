from django.contrib import admin
from .models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'descr', 'img')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'descr')
    list_filter = ('name', )
    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'descr', 'img', 'hours', 'price', 'category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'descr')
    list_filter = ('price', )

class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'worker_count', 'hour_price')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('worker_count', 'hour_price')

class ChiefAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'experience')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('experience', )

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'img', 'category')
    search_fields = ('category',)
    list_filter = ('category', )    

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'category')
    search_fields = ('category',)
    list_filter = ('category', )     

admin.site.register(Category, CategoryAdmin)    
admin.site.register(Service, ServiceAdmin)
admin.site.register(Brigade, BrigadeAdmin)
admin.site.register(Chief, ChiefAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Feedback, FeedbackAdmin)