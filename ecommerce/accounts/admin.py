from django.contrib import admin
from .models import User
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('phone_number', 'email', 'is_admin')
    list_filter = ('is_admin',)
    search_fields = ('phone_number', 'email')
    ordering = ('email',)
    filter_horizontal = ()

    fieldsets = (
        ('Base', {'fields': ('phone_number', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'age', 'sex', 'avatar', 'bio')}),
        ('Permissions', {'fields': ('is_admin', 'last_login', 'is_active')}),
    )

    add_fieldsets = (
        ('Base', {'fields': ('phone_number', 'email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'age', 'sex', 'avatar', 'bio')}),
        ('Permissions', {'fields': ('is_admin', 'last_login', 'is_active')}),
    )


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
