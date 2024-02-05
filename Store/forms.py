from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form_control","placeholder":"Enter your username"}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form_control","placeholder":"Enter your first_name"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form_control","placeholder":"Enter your last_name"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form_control","placeholder":"Enter your email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form_control","placeholder":"Enter your password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form_control","placeholder":"confirm password"}))
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form_control","placeholder":"Enter your username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form_control","placeholder":"Enter yout password"}))
    
class OrderForm(forms.Form):
    address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"address","rows":5}))
    
