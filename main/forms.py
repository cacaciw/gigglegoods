from django.forms import ModelForm
from main.models import GiggleCatalogue

class GiggleForm(ModelForm):
    class Meta:
        model = GiggleCatalogue
        fields = ["name", "price", "description", "giggleLevel"]