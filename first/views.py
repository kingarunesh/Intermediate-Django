from django.shortcuts import render
from django.http import HttpResponseRedirect

from first.models import Student
from first.forms import FirstForm, SecondForm, ThirdForm, FourForm, FiveForm


def first(request):
    """
        first page view
    """
    # students = Student.objects.all()
    
    #NOTE :     id and for change | label suffix change | initial input value
    # first_form = FirstForm()
    # first_form = FirstForm(auto_id=True)
    # first_form = FirstForm(auto_id=False)
    # first_form = FirstForm(auto_id="hello_%s")
    # first_form = FirstForm(auto_id=True, label_suffix="")
    # first_form = FirstForm(auto_id=True, label_suffix=" : ")
    # first_form = FirstForm(auto_id=True, label_suffix=" : ", initial={"name": "Arunesh", "email": "arunesh@gmail.com"})
    
    # first_form = FirstForm()
    # first_form = FirstForm(field_order=None)
    # first_form = FirstForm(field_order=["email", "first_name", "section"])
    # first_form.order_fields(field_order=["email", "first_name", "section"])
    
    
    # second_form = SecondForm()
    
    # third_form = ThirdForm()
    
    # four_form = FourForm()
    
    
    if request.method == "POST":
        five_form = FiveForm(request.POST)
        
        if five_form.is_valid():
            # print(five_form.cleaned_data)
            print(five_form.cleaned_data["name"])
            print(five_form.cleaned_data["email"])
            print(five_form.cleaned_data["password"])
            
            return render(request=request, template_name="first/success.html")
            
            # return HttpResponseRedirect("/success/")
    else:
        five_form = FiveForm()
        print("GET requets")
    
    context = {
        # "students": students,
        # "first_form": first_form,
        # "second_form": second_form,
        # "third_form": third_form,
        # "four_form": four_form,
        "five_form": five_form
    }
    
    
    return render(request=request, template_name="first/first.html", context=context)



def thankyou(request):
    return render(request=request, template_name="first/success.html")