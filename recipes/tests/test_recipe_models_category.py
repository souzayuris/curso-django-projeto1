from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeTestBase


class RecipeCategoryModelTest(RecipeTestBase):

    def setUp(self) -> None:
        self.category = self.make_category(
            name='Category Testing'
        )
        return super().setUp()
    
    def test_recipe_category_model_string_representation(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )
    
    def test_recipe_category_model_name_max_lenght_is_65_chars(self):
        self.category.name = 'A' * 66
        
        #Testa se vai levantar Erro de Validação no campo nome com mais de 65 caracters
        with self.assertRaises(ValidationError):
            self.category.full_clean()
