from django.contrib import admin
from supports.models import Restaurant, Dish

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenumber', 'address','opentime','closetime')

    search_fields = ['name', 'address']

admin.site.register(Restaurant, RestaurantAdmin)

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'SN', 'restaurant','description','price','onshelf','supper')

    search_fields = ['name','restaurant' ,'description']

admin.site.register(Dish, DishAdmin)