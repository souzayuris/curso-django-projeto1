from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeModelTest(RecipeTestBase):

    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A'*70

        with self.assertRaises(ValidationError):
            self.recipe.full_clean() #Aqui a validação de limite de caracter ocorre

    def make_recipe_no_defaults(self):
        recipe = Recipe(
                    category=self.make_category(name='Test Default Category'), 
                    author=self.make_author(username='newUser'),
                    title='Titulo',
                    description='Recipe-description', 
                    slug='Recipe-slug-test',
                    preparation_time=1,
                    preparation_time_unit='minutos',
                    servings=5,
                    servings_unit='pratos',
                    preparation_steps=5,
                    cover='cover'
        )
        recipe.full_clean()
        recipe.save
        return recipe

    #Usado para testes que necessitam de FOR
    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ])
    def test_recipe_fields_max_lenght(self, field, max_lenght):

        setattr(self.recipe, field, 'A' * (max_lenght + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean() 

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg="Recipe preparation steps is not false"
        )

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.is_published,
            msg="Recipe is published is not false"
        )
    
    def test_recipe_string_representation(self):
        needed = 'Testing Representatation'
        self.recipe.title = 'Testing Representatation'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), 'Testing Representatation',
                         msg = 'Recipe string representation must be {needed}'
                         )