from django.contrib import admin
from .models import Ingredient, Recipe

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

class RecipeIngredient(admin.ModelAdmin):
    model = RecipeAdmin