from django.contrib import admin
from recipeboxapp.models import Author
from recipeboxapp.models import Recipe
# Register your models here.
admin.site.register(Author)
admin.site.register(Recipe)
