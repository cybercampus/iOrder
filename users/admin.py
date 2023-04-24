from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'ticket')

    search_fields = ['username' ]

admin.site.register(User, UserAdmin)