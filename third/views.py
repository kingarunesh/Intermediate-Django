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