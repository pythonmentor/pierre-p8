from django.test import TestCase
from .models import Product

class ProductViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name="Test Product", category="cat1", nutrition_grade="e")
        for category in ["cat1", "cat2", "cat3", "cat4"]:
            for grade in ["a", "b", "c", "d", "e"]:
                for e in range(60):  # Creating 60 instances for each different grades
                    Product.objects.create(nutrition_grade=grade, category=category)

    def test_product(self):
        response = self.client.get('/products/product/1')
        self.assertEquals(response.context['prod'], Product.objects.get(pk=1))
        self.assertEquals(response.status_code, 200)
        # When launching all tests only : products.models.Product.DoesNotExist: Product matching query does not exist. ;

    def test_search_product(self):
        # Testing with correct input
        response = self.client.post('/products/search', {'research':'Test Product'})
        self.assertEquals(response.status_code, 200)
        # Testing with incorrect input
        response = self.client.post('/products/search', {'research':'WrongInput'})
        self.assertEquals(response.status_code, 302)

#TODO: Se renseigner sur le fonctionnement de setUpTestData => Error quand je lance tout les tests ensembles, pas d'erreur quand je les lance individuellement