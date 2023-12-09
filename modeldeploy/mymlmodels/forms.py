from django import forms


class SMILESForm(forms.Form):
    
    SMILES = forms.CharField(label='SMILES', max_length=500, required=True)