from django.forms import ModelForm
from .models import order

class orderform(ModelForm):
    class Meta:
        model = order
        fields = '__all__'