from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'surname')
