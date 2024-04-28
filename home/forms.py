from .models import Contact
from django import forms



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name*'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email*'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message*'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
