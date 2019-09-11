from django import forms
from .models import Todo
class todoForm(forms.ModelForm):

    class Meta:
        model=Todo

        fields=('text','title','link_code','lang')
        labels={'title':'Paste Title','text':'New Paste','link_code':'Paste Code','lang': 'Syntax Highlighting'}
        #widgets={'lang': forms}
        