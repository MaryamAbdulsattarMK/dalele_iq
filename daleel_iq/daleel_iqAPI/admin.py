from django.contrib import admin

# Register your models here.
from .models import myUser


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'auth_provider', 'created_at']


admin.site.register(myUser, UserAdmin)