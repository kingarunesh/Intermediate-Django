from django import forms
from django.core import validators


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



class FiveForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    


class SixForm(forms.Form):
    # empty_value="Arunesh"
    name = forms.CharField(min_length=3, max_length=50, strip=True, error_messages={"required": "Please enter your name."})
    agree = forms.BooleanField(label="I Agree", required=False)
    roll = forms.IntegerField(min_value=100, max_value=1000)
    price = forms.DecimalField(min_value=1, max_value=100, max_digits=4, decimal_places=1)
    rate = forms.FloatField(min_value=5, max_value=50)
    comment = forms.SlugField()
    email = forms.EmailField(min_length=5, max_length=50)
    website = forms.URLField()
    password = forms.CharField(widget=forms.PasswordInput)
    description = forms.CharField(widget=forms.Textarea) 



class SevenForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_name(self):
        value = self.cleaned_data["name"]
        
        if len(value) < 3:
            raise forms.ValidationError("Please enter more than or equal to 3 character")
        
        return value
    
    
    def clean_email(self):
        print(len(self.cleaned_data["email"]))
        
        value = self.cleaned_data["email"]
        
        if len(value) < 20:
            raise forms.ValidationError("Please enter valid email address")
        return value


#SECTION :      nine form

def starts_with_a(value):
    if value[0] != "a":
        raise forms.ValidationError("Name must be starts with 'a'")


class NineForm(forms.Form):
    #NOTE :         custom and build validators
    # name = forms.CharField(validators=[validators.MaxLengthValidator(20), starts_with_a])
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    
    def clean(self):
        cleaned_data = super().clean()
        
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        
        if len(name) < 4:
            raise forms.ValidationError("Name must be more than 3 or equal to 3")
        
        if name[0] != "a":
            raise forms.ValidationError("Name must be starts with 'a'")
        
        if len(email) < 10:
            raise forms.ValidationError("Email must be greater than or equal to 10")
        
        if len(password) <= 10:
            raise forms.ValidationError("Password must be greater than or equal to 10")

        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm-Password is equal.")


class TenForm(forms.Form):
    name = forms.CharField(error_messages={"required": "Please Enter name."})
    email = forms.EmailField(error_messages={"required": "Please Enter valid Email"}, min_length=10, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, error_messages={"required": "Please Enter Correct Password"})