from django import forms
from .models import WerckerModels
class WerckerForm(forms.ModelForm):

   TokeName = forms.CharField(
                    #max_length=20,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'Link Name / Anchor Text',
                    }),
                    required=True)
   Token = forms.CharField(
                    #max_length=200,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'Link Name / Anchor Text',
                    }),
                    required=True)
   class Meta:
       model = WerckerModels
       fields = ('TokeName','Token',)



