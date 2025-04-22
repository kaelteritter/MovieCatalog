from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class SingUpForm(forms.ModelForm):
    error_messages = {
        'no_password_confirmation': 'Пароль не введен повторно',
        'password_mismatch': 'Пароли не совпадают',
    }

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(),
        strip=False,
        help_text='Введите пароль'
        )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(),
        strip=False,
        help_text='Повторите пароль для подтверждения'
        )

    class Meta:
        model = User
        fields = ['email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not password2:
            raise forms.ValidationError(
                self.error_messages['no_password_confirmation'],
                code='no_password_confirmation'
            )
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'], 
                code='password_mismatch'
            )
        
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            if hasattr(user, 'save_m2m'):
                self.save_m2m()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update(
                    {
                    'class': 'form-control',
                    'placeholder': 'name@example.com',
                    }
                )