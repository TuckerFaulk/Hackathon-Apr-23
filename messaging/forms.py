from django import forms


class ComposeMessageForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ReplyMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
