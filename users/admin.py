from django.contrib import admin
from .models import CustomUser, Skill

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'gender', 'get_skills']
    
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(CustomUser, CustomUserAdmin)