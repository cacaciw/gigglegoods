from django.forms import ModelForm
from main.models import GiggleCatalogue

class GiggleForm(ModelForm):
    class Meta:
        model = GiggleCatalogue
        fields = ["product", "price", "description", "giggle_level"]