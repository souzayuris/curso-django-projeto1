from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeDetailViewTest(RecipeTestBase):
       
    def test_recipe_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
            )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_correct_recipe(self):

        title = 'This is a detail page'

        self.make_recipe(title=title)
        
        response = self.client.get(reverse('recipes:recipe', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(title, content)


