from django.contrib import admin

# Register your models here.
# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (*UserAdmin.fieldsets, ('Roles', {'fields': ('is_observer','is_action_owner','is_safety_manager')}),)
    list_display = ('username','email','is_observer','is_action_owner','is_safety_manager')
