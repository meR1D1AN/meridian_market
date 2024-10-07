from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "is_active")
    search_fields = ("name", "email")
    list_filter = ("is_active",)
