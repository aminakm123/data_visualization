from django import forms
from dashboard.models import DataPoint

class DataPointForm(forms.ModelForm):
    class Meta:
        model = DataPoint
        fields = ['start_year','intensity','topic','sector','region']
        widgets = {
            'start_year': forms.TextInput(attrs={'class':'form-control'}),
            'intensity': forms.TextInput(attrs={'class':'form-control'}),
            'topic': forms.TextInput(attrs={'class':'form-control'}),
            'sector': forms.TextInput(attrs={'class':'form-control'}),
            'region': forms.TextInput(attrs={'class':'form-control'}),
        }