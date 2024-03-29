from django.test import TestCase

from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):

    def setUp(self) -> None:

        return super().setUp()
    
    
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)
    
    def make_author(
                    self,
                    first_name = 'user',
                    last_name = 'name',
                    username = 'username',
                    password = '123',
                    email = 'email@gmail.com',
                    ):
        
        return User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            email = email,
        )
    
    def make_recipe(self, 
                    category_data=None, 
                    author_data=None,
                    title='Titulo',
                    description='Recipe-description', 
                    slug='Recipe-slug',
                    preparation_time=1,
                    preparation_time_unit='minutos',
                    servings=5,
                    servings_unit='pratos',
                    preparation_steps=5,
                    preparation_steps_is_html=False,
                    is_published=True,
                    cover='cover'
                    ):
                
        if category_data is None:
            category_data = {}
                    
        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data), 
            author=self.make_author(**author_data),
            title=title,
            description=description, 
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover=cover
        ) 