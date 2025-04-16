from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class SingUpForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                    {
                    'class': 'form-control',
                    'placeholder': 'name@example.com',
                    }
                )