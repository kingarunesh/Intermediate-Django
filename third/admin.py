from django.contrib import admin

from third.models import FirstModel, User


@admin.register(FirstModel)
class ThirdModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "password"]
    list_display_links = ["id", "name", "email", "password"]



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["t_name", "s_name", "email", "password"]
    list_display_links = ["t_name", "s_name", "email", "password"]