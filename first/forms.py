from django import forms


class FirstForm(forms.Form):
    first_name = forms.CharField()
    section = forms.CharField()
    email = forms.EmailField()


class SecondForm(forms.Form):
    name = forms.CharField(initial="Hello", help_text="This is help text")


class ThirdForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    key = forms.CharField(widget=forms.HiddenInput())


class FourForm(forms.Form):
    first_name = forms.CharField(label="First Name", label_suffix=" ", initial="Arunesh", required=False, disabled=True, help_text="This is help text")
    
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    key = forms.CharField(widget=forms.HiddenInput)
    message = forms.CharField(widget=forms.Textarea(attrs={"cols": 50, "rows": 4, "class": "message", "id": "message"}))
    photo = forms.CharField(widget=forms.FileInput)