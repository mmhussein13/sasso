from django import forms
from .models import Account, UserProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' ',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' ',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = [
            'first_name', 'last_name',
            'phone_number', 'email', 'password', 'confirm_password'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match. Please try again.")
            self.add_error(None, "Please ensure both passwords are identical.")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        placeholder_map = {
            'first_name': ' ',
            'last_name': ' ',
            'email': ' ',
            'phone_number': ' ',
        }
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control border-0'
            if field in placeholder_map:
                self.fields[field].widget.attrs['placeholder'] = placeholder_map[field]



class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False, error_messages={'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = (
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'gender',
            'country',
            'profile_image'
        )
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
