from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Project
from .models import Message 

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)
    phone = forms.CharField(label='Telefon')
    address = forms.CharField(label='Adres')
    city = forms.CharField(label='Miasto')

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie pasują do siebie!')
        return cd['password2']
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ProfileEditForm(forms.ModelForm):
    class Meta: 
     model = UserProfile
     fields = ['phone', 'address', 'city']






class ProjectForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
                               
    class Meta:
      model = Project
      fields = ['name', 'description', 'start_date', 'end_date', 'stakeholders', 'status']







class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']
