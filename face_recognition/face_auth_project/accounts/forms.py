from django import forms
from django.contrib.auth.models import User
# Django’s built-in registration form that already handles: password hashing, (password1 and password2) basic validation
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    # Uses an EmailInput widget, which renders as <input type="email">.
    # Adds Bootstrap CSS class and placeholder for styling
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    first_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))

    # Defines which model and fields the form will save to
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        # Customizes the appearance of the username field. Sets CSS class and placeholder for Bootstrap styling.
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
        }

    # The __init__ method is called when the form is created. It first calls the parent class constructor (to initialize the default behavior).
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })

    # Overrides the default save() to add more behavior before saving.
    # commit=False → creates the user object but doesn’t save it yet (lets you modify it first).
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

# Used for logging in using facial recognition — so the user provides a username.
class FaceLoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'required': True
    }))