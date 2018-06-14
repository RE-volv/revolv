from django.contrib import admin

from .models import RevolvUserProfile


class UserAdmin(admin.ModelAdmin):
    search_fields = ['user__username']

admin.site.register(RevolvUserProfile, UserAdmin)
