from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['user_wishlist']

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'
