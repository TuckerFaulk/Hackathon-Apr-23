from django import forms
from .models import Message


class ComposeMessageForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ReplyMessageForm(forms.ModelForm):
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Reply message...',
            'rows': 5,
        }),
        required=True,
    )

    class Meta:
        model = Message
        fields = ('message',)
