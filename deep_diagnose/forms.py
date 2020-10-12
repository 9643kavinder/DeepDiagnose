from django import forms
from .models import Profile
from django.contrib.auth.models import User


class Location(forms.Form):
    city = forms.CharField(

        label='City',
        max_length=32
    )
    state = forms.CharField(

        label='State',
        max_length=32
    )


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )


class OrderNowForm(forms.Form):

    user_name = forms.CharField(max_length=125,
                                label='Username',)
    email_id = forms.EmailField(required=True,
                                label='Email Id',)
    age = forms.CharField(max_length=20)
    address_line_1 = forms.CharField(max_length=125,
                                     label='Address Line !',)
    city = forms.CharField(max_length=125,
                           label='City',)
    state = forms.CharField(max_length=125,
                            label='State',)
    zip_code = forms.CharField(required=True,
                                  label='Zip Code',max_length=20)
    phone_no = forms.CharField(max_length=12,
                                  label='Phone Number', )
    suitable_date = forms.CharField(max_length=20,
                                    label='Suitable Date',)
    suitable_time = forms.CharField(max_length=20,
                                    label='Suitable Time',)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class LoginForm(forms.Form):
    username = forms.CharField(label=(u'Username'))
    password = forms.CharField(label=(u'Pasword'), widget=forms.PasswordInput(render_value=False))