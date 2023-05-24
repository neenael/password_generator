from .models import PasswordData
from django import forms


class PasswordForm(forms.ModelForm):

    MODE_CHOICES = (
        ('common_password', 'Символьный пароль'),
        ('XKCD_password', 'Словестный пароль')
    )
    mode = forms.ChoiceField(
        choices=MODE_CHOICES,
        widget=forms.Select(
            attrs={
                'name': "mode",
                'id': "choices_mode",
                'class': "mode_input password_input choices choices_mode",
                'required': True
            }
        )
    )
    COMPLEXITY_CHOICES = (
        ('digit', 'Только цифры'),
        ('digit_alpha', 'Цифры и буквы'),
        ('complex', 'Все символы'),
    )
    complexity = forms.ChoiceField(
        choices=COMPLEXITY_CHOICES,
        widget=forms.Select(
            attrs={
                'name': "complexity",
                'id': "choices_complexity",
                'class': "complexity_input password_input active choices choices_complexity",
            }
        )
    )

    class Meta:
        model = PasswordData
        fields = ('length', 'mode', 'complexity')

        widgets = {
            'length': forms.TextInput(attrs={'class': 'length_input password_input', 'type': 'number', 'name': 'length', 'min': '1', 'max': '999', 'placeholder': '...', 'required': True, 'id': 'length_input'}),
            'complexity': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'})
        }
