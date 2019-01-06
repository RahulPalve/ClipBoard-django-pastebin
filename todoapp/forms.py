from django import forms
from .models import Todo
class todoForm(forms.ModelForm):

    class Meta:
        model=Todo
        fields=('text','title','link_code',)
        labels={'text':'New Paste','title':'Paste Title','link_code':'Paste Code (enter any alphanumeric text upto  8 characters)'}
        
        