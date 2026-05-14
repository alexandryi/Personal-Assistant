from django import forms
from .models import Contact, Phone
import re

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact

        fields = [
            "name",
            "email",
            "phone",
            "address",
            "birthday",
        ]

        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"})
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        pattern = r'^\+?[0-9]{10,15}$'

        if not re.match(pattern, phone):
            raise forms.ValidationError(
                "Incorrect phone number"
            )

        return phone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['number']