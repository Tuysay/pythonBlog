from django import forms
from .models import Commit

class CommitForm(forms.ModelForm):
    class Meta:
        model = Commit
        fields = ('name', 'email', 'text')
