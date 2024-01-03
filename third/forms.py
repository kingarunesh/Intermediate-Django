from django import forms

from third.models import FirstModel, SecondModel, User


class FirstForm(forms.ModelForm):
    
    #NOTE :     over-write fields
    name = forms.CharField(max_length=100, required=False)
    
    class Meta:
        model = FirstModel
        fields = ["name", "email", "password"]
        
        labels = {
            "name": "Enter Your Name",
            "email": "Enter Your Email Address",
            "password": "Enter Your Password"
        }
        
        # label_suffix = {
        #     "name": "-"
        # }
        
        help_text = {
            "name": "Arunesh"
        }
        
        error_messages = {
            "name": {"required": "Please Enter Your Valid Name."},
            "email": {"required": "Please Enter Your Valid Email Address"},
            "password": {"required": "Please Enter Your Valid Password"}
        }
        
        widgets = {
            "password": forms.PasswordInput,
            "name": forms.TextInput(attrs={"class": "name_style", "placeholder": "Your Name..."})
        }
    


class SecondForm(forms.ModelForm):
    class Meta:
        model = SecondModel
        # fields = ["name", "email", "password"]
        # fields = "__all__"
        exclude = ["name"]




class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["s_name", "email", "password"]


class TeacherForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["t_name", "email", "password"]