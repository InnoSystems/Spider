from django.test import TestCase

from .models import Shopping

class ShoppingTest(TestCase):
    
    def test_create_shopping(self):
        shopping = Shopping(store_name="edeka")
        self.assertIs(shopping.store_name, "edeka2")