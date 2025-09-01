import unittest
from coffee_menu import CoffeeMenu 

class TestCoffeeMenu(unittest.TestCase):

    def setUp(self):
        self.menu = CoffeeMenu()

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('latte'), 2.75)

    def test_get_price_non_existing_item(self):
        with self.assertRaises(KeyError):
            self.menu.get_price('pizza')

    def test_add_item(self):
        self.menu.add_item('helado', 1.20)
        self.assertEqual(self.menu.menu['helado'], 1.20)


if __name__ == '__main__':
    unittest.main()