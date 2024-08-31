from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import MyUser

        
class SignupForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['full_name','phone','national_code','adress','date_of_birth','password']
    
    password_again = forms.CharField(strip=False, widget=forms.PasswordInput)
    date_of_birth = forms.DateField(label="date of birth (optional)",required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        pas1 = cleaned_data.get("password")
        pas2 = cleaned_data.get("password_again")

        if pas1 != pas2:
            raise ValidationError("Passwords are not the same")
    
    def clean_national_code(self):
        national_code = self.cleaned_data.get('national_code')
        if MyUser.objects.filter(national_code=national_code).exists():
            raise forms.ValidationError('User with this National code already exists.')
        return national_code
        
class LoginForm(forms.Form):
    national_code = forms.CharField()
    # password = forms.PasswordInput()
    password = forms.CharField(strip=False, widget=forms.PasswordInput)

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = MyUser
        fields = ["full_name", "date_of_birth","adress","national_code","phone"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ["national_code","adress","full_name", "password", "date_of_birth", "is_active", "is_admin"]


class ForgetPasswordForm1(forms.Form):
    code = forms.CharField()
    
    def clean_code(self):
        n_code = self.cleaned_data.get('code')
        if not MyUser.objects.filter(national_code=n_code).exists():
            self.add_error('code', 'national_code is not corect.')
        return n_code
    
class ForgetPasswordForm2(forms.Form):
    code = forms.CharField()
    
    
class ChengePasswordForm(forms.Form):
    pas1 = forms.CharField(label="password")
    pas2 = forms.CharField(label="password agane")
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('pas1') != cleaned_data.get('pas2'):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    