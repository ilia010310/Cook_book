from django.contrib import admin
from .models import Product, Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    exclude = ('recipe_ingredients',)
    inlines = [RecipeIngredientInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'times_used')

admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(RecipeIngredient)