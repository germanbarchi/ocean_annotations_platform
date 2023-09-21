from django import forms
from pair_comparison.models import Annotation

DIMENSIONS = {'dim_O': 'Apretura a la experiencia', 
              'dim_C': 'Responsabilidad', 
              'dim_E': 'Extraversion', 
              'dim_A': 'Amabilidad',
              'dim_N': 'Neuroticismo'}
CHOICES = [('A', 'A'), ('B', 'B')]

HELPS = {'dim_O' : 'Dim O help',
         'dim_C' : 'Dim C help',
         'dim_E' : 'Dim E help',
         'dim_A' : 'Dim A help',
         'dim_N' : 'Dim N help',}

class AnnotationForm(forms.ModelForm):
    dim_O = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), required=True)
    dim_C = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), required=True)
    dim_E = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), required=True)
    dim_A = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), required=True)
    dim_N = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), required=True)
    
    
    class Meta:
        model = Annotation
        exclude = ('submit', 'audio_A', 'audio_B',  'order', 'user','last_modified')

    def __init__(self, *args, **kwargs):
        super(AnnotationForm, self).__init__(*args, **kwargs)
        for dim in DIMENSIONS:
            self.fields[dim].help_text = HELPS[dim]