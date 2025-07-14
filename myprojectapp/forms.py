from django import forms
from .models import TShirt

class TShirtForm(forms.ModelForm):
    class Meta:
        model = TShirt
        fields = ['name', 'description', 'color', 'size', 'design_image']
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Your custom text...',
                'class': 'form-control',
                'style': 'opacity: 0.6;',
                'rows': 3,
            }),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'design_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TShirtForm, self).__init__(*args, **kwargs)
        if 'size' in self.fields:
            self.fields['size'].widget.attrs.update({'class': 'form-control'})
        if 'image' in self.fields:
            self.fields['image'].widget.attrs.update({'class': 'form-control'})