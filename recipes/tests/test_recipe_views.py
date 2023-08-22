from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeViewsTest(RecipeTestBase):
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_corret_template(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        
        self.make_recipe()
        
        Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>Not Found</h1>',
            response.content.decode('utf-8')
        )  
    def test_recipe_home_template_loads_recipes(self):
        
        self.make_recipe()

        response = self.client.get(reverse('recipes:home'))
        response_recipes = response.context['recipes']
        content = response.content.decode('utf-8')

        self.assertEqual(response_recipes[0].title, 'Titulo')
        self.assertIn('minutos', content)

    
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
            )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        title = 'This is a category test'

        self.make_recipe(title=title)
        
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

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

    def test_recipe_home_template_dont_load_recipes_not_published(self):

        self.make_recipe(is_published=True)

        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            '1 minutos',
            response.content.decode('utf-8')
        )  