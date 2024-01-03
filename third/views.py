from django.shortcuts import render

from third.models import FirstModel
from third.forms import FirstForm


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