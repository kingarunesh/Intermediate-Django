from django.shortcuts import render

from second.forms import FirstForm
from second.models import Second


def second(request):
    
    #NOTE :     read entry
    entries = Second.objects.all()
    
    if request.method == "POST":
        form = FirstForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
        
            #NOTE :     insert entry
            newEntry = Second(name=name, email=email, password=password)
            newEntry.save()
            
            
            #NOTE :     update entry
            # updateEntry = Second(id=1, name=name, email=email, password=password)
            # updateEntry.save()
            
            #NOTE :     delete entry
            # deleteEntry = Second(id=1)
            # deleteEntry.delete()
            
    else:
        form = FirstForm()
    
    context = {
        "form": form,
        "entries": entries
    }  
    
    return render(request=request, template_name="second/second.html", context=context)