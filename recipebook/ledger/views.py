from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

class recipe_list(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

class recipe(DetailView):
    model = Recipe
    template_name = 'recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.ingredients.all()
        return context