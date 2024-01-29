from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Recipe, RecipeIngredient, Product


def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)

    recipe_ingredient, created = RecipeIngredient.objects.get_or_create(recipe=recipe,
                                                                        product=product)

    if not created:
        recipe_ingredient.weight_in_grams = weight
        recipe_ingredient.save()

    return HttpResponse(f'<h2>Добавление прошло успешно!</h2>')

def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')

    recipe = get_object_or_404(Recipe, id=recipe_id)

    ingredients = RecipeIngredient.objects.select_for_update().filter(recipe=recipe)

    for ingredient in ingredients:
        ingredient.product.times_used += 1
        ingredient.product.save()

    return HttpResponse('<h2>Блюдо успешно приготовлено</h2>')

def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    name = Product.objects.get(id=product_id)

    recipes_without_product = Recipe.objects.select_for_update().exclude(recipeingredient__product_id=product_id)
    recipes_less_than_10g = Recipe.objects.select_for_update().filter(recipeingredient__product_id=product_id,
                                                                      recipeingredient__weight_in_grams__lt=10)

    context = {
        'recipes_without_product': recipes_without_product,
        'recipes_less_than_10g': recipes_less_than_10g,
        'product': name,
    }

    return render(request, 'show_recipes.html', context)







