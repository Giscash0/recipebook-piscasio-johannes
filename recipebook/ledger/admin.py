from django.contrib import admin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, Profile

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(admin.ModelAdmin):
	inlines = [ProfileInline]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)