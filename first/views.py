from django.shortcuts import render

from first.models import Student
from first.forms import FirstForm, SecondForm, ThirdForm, FourForm


def first(request):
    """
        first page view
    """
    students = Student.objects.all()
    
    #NOTE :     id and for change | label suffix change | initial input value
    # first_form = FirstForm()
    # first_form = FirstForm(auto_id=True)
    # first_form = FirstForm(auto_id=False)
    # first_form = FirstForm(auto_id="hello_%s")
    # first_form = FirstForm(auto_id=True, label_suffix="")
    # first_form = FirstForm(auto_id=True, label_suffix=" : ")
    # first_form = FirstForm(auto_id=True, label_suffix=" : ", initial={"name": "Arunesh", "email": "arunesh@gmail.com"})
    
    first_form = FirstForm()
    # first_form = FirstForm(field_order=None)
    # first_form = FirstForm(field_order=["email", "first_name", "section"])
    first_form.order_fields(field_order=["email", "first_name", "section"])
    
    
    second_form = SecondForm()
    
    third_form = ThirdForm()
    
    four_form = FourForm()
    
    context = {
        "students": students,
        "first_form": first_form,
        "second_form": second_form,
        "third_form": third_form,
        "four_form": four_form
    }
    
    return render(request=request, template_name="first/first.html", context=context)
