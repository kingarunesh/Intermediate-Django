from django.contrib import admin

from third.models import FirstModel


@admin.register(FirstModel)
class ThirdModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "password"]
    list_display_links = ["id", "name", "email", "password"]