from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post,Comment
class SignUp(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'})}

class Login(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,
            widget=forms.PasswordInput(attrs={'class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title','content'}
        labels = {'title':'Title','content':'Content'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                'content':forms.Textarea(attrs={'class':'form-control'})}

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'name','com'}
        labels = {'name':'Name','com':'Comment'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
                'com':forms.Textarea(attrs={'class':'form-control'})}