# registro/forms.py
from django import forms
from .models import DatosPersonales, Bloque2Trayectoria, Bloque3CaracteristicasEscuela, Bloque4EntornoSocial
from django.contrib.auth.models import User

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        exclude = ('registro',)
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
class Bloque2TrayectoriaForm(forms.ModelForm):
    class Meta:
        model = Bloque2Trayectoria
        exclude = ['usuario']
        widgets = {
            'area': forms.TextInput(attrs={'placeholder': 'Ej. Físico-matemático'}),
            'motivo_beca': forms.TextInput(attrs={'placeholder': 'Motivo de la beca'}),
        }


class Bloque3Form(forms.ModelForm):
    class Meta:
        model = Bloque3CaracteristicasEscuela
        exclude = ['usuario']        
        
class Bloque4Form(forms.ModelForm):
    class Meta:
        model = Bloque4EntornoSocial
        exclude = ['usuario']    

class RegistroUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return cleaned            