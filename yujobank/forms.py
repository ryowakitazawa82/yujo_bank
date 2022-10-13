from django import forms
from .models import YujoBank


class YujoBankForm(forms.ModelForm):
    class Meta:
        model = YujoBank
        fields = ('date', 'title', 'text',)
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }