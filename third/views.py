from django.shortcuts import render

from third.models import FirstModel, SecondModel, User
from third.forms import FirstForm, SecondForm, StudentForm, TeacherForm


def third_view(request):
    
    if request.method == "POST":
        form = FirstForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            #NOTE :     insert new entry
            # insert_entry = FirstModel(name=name, email=email, password=password)
            # insert_entry.save()
            
            #NOTE :     update entry
            # update_entry = FirstModel(id=1, name=name, email=email, password=password)
            # update_entry.save()
            
            #NOTE :     delete entry
            delete_entry = FirstModel(id=1)
            delete_entry.delete()
            
    else:
        form = FirstForm()
    
    return render(request=request, template_name="third/third.html", context={"form": form})



def hello(request, first_id, second_id, my_slug, check, year):
    
    print(first_id)
    print(type(first_id))
    
    print()
    
    print(second_id)
    print(type(second_id))
    
    print()
    
    print(my_slug)
    print(type(my_slug))
    
    print()
    
    #!      this is not related URL
    print(check)
    
    print()
    
    print(year)
    print(type(year))
        
    return render(request=request, template_name="third/hello.html")



def second_view(request):
    
    form = SecondForm()
    
    return render(request=request, template_name="third/second.html", context={"form": form})



def student_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
    
    form = StudentForm()
    
    return render(request=request, template_name="third/student.html", context={"form": form})


def teacher_view(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        
        if form.is_valid():
            form.save()
    
    form = TeacherForm()
    
    return render(request=request, template_name="third/teacher.html", context={"form": form})