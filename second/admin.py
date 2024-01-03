from django.contrib import admin

from second.models import Second


@admin.register(Second)
class SecondAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "password"]
    list_display_links = ["id", "name", "email", "password"]