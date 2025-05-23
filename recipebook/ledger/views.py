from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm, IngredientFormSet

class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_add_recipe'] = True
        return context

class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.ingredients.all()
        return context