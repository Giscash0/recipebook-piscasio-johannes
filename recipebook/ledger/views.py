from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

def recipe_list(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

def recipe(request, num=1):
    return render(request, 'recipe.html', {"recipe": recipes[num-1]})