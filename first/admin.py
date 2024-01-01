from django.contrib import admin

from first.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "student_id", "name", "email", "marks", "section"]
    list_display_links = ["id", "student_id", "name"]



# class StudentAdmin(admin.ModelAdmin):
#     list_display = ["id", "student_id", "name", "email", "marks", "section"]

# admin.site.register(Student, StudentAdmin)
