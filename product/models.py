from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Товар')
    times_used = models.IntegerField(verbose_name='Количество', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']

class Recipe(models.Model):
    name = models.CharField(max_length=30, verbose_name='Рецепт')
    recipe_ingredients = models.ManyToManyField('RecipeIngredient', related_name='recipes')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['id']




class RecipeIngredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    weight_in_grams = models.IntegerField(verbose_name='Вес в граммах')

    class Meta:
        unique_together = ('product', 'recipe')


    def __str__(self):
        return f"{self.product.name} - {self.weight_in_grams}g"

