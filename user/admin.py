from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'company_name')
    list_filter = ('user_type',)
    search_fields = ('user__username', 'company_name')
