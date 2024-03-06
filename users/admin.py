from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'first_name', 'last_name', 'address', 'user_role')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'address')
    readonly_fields = ('id',)
    filter_horizontal = ()
    list_filter = ('user_role',)

admin.site.register(User, CustomUserAdmin)

