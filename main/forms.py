from django.forms import ModelForm
from main.models import GiggleCatalogue
from django.utils.html import strip_tags

class GiggleForm(ModelForm):
    class Meta:
        model = GiggleCatalogue
        fields = ["name", "price", "description", "giggleLevel"]

        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)

        def clean_price(self):
            price = self.cleaned_data["price"]
            return strip_tags(price)
        
        def clean_desc(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)
        
        def clean_giggle(self):
            giggleLevel = self.cleaned_data["giggleLevel"]
            return strip_tags(giggleLevel)