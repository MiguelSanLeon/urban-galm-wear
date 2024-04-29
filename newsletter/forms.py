from django import forms
from .models import Subscriber


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email*'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
