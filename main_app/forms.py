from django.forms import ModelForm, NumberInput, CharField
from .models import Widget

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']
        widgets = {
            'quantity': NumberInput()
        }