from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('username', 'createdate', 'dish','quantity','spicy','dinnertime')

    search_fields = ['username','dish' ]

admin.site.register(Order, OrderAdmin)
