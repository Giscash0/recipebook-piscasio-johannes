from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, RecipeImage, RecipeIngredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

IngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    fields=('ingredient', 'quantity'),
    extra=1,
    can_delete=False
)