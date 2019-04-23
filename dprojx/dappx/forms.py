from django import forms
from dappx.models import UserProfileInfo, Object
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')

class ObjectForm(forms.ModelForm):
    class Meta():
         model = Object
         fields = ('name','description', 'activated', 'slug')
