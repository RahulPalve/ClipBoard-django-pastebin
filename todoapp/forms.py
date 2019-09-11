from django import forms
from .models import Todo
class todoForm(forms.ModelForm):

    class Meta:
        model=Todo

        fields=('title','text','link_code','lang')
        labels={'title':'Paste Title','text':'New Paste','link_code':'Paste Code (enter any alphanumeric text upto  8 characters)','lang': 'Language'}
        #widgets={'lang': forms}
        