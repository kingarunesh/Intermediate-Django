from django.shortcuts import render

from first.models import Student


def first(request):
    """
        first page view
    """
    students = Student.objects.all()
    
    context = {
        "students": students
    }
    
    return render(request=request, template_name="first/first.html", context=context)
