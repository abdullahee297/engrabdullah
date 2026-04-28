<<<<<<< HEAD
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
=======
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
>>>>>>> bcabad9afcce1d08ec24b6a85be487c198b25228
    message = forms.CharField(widget=forms.Textarea)