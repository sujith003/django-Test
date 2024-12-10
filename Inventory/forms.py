from django.forms import ModelForm
from .models import *

class product_Form(ModelForm):

    class Meta:

        model = Product
        fields= '__all__'