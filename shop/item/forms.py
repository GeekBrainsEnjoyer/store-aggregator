from django import forms


from .models import Item

INPUT_CLASSES = 'w-full py-2 px-7 rounded-xl'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'placeholder': "Input item's name",
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'placeholder': "Input item's description",
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'placeholder': "Input item's price",
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
