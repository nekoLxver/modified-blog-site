from django import forms


class SendEmailForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(max_length=250, required=False, widget=forms.Textarea)