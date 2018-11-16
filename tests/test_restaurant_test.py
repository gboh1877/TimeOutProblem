from unittest import TestCase
from main import restaurant_test

class TestRestaurant_test(TestCase):
    def test_restaurant_nothing_to_eat(self):
        self.assertEqual(restaurant_test({"name":"test","food":["test"],"drinks":["test"]},
                                         [{"name":"test","wont_eat":["test"],"drinks":["test"]}]),
                                         ["There is nothing for test to eat"])
    def test_restaurant_noting_to_drink(self):
        self.assertEqual(restaurant_test({"name":"test","food":["test"],"drinks":["test"]},
                                         [{"name":"test","wont_eat":[],"drinks":["test1"]}]),
                                         ["There is nothing for test to drink"])
    def test_restaurant_fine(self):
        self.assertFalse(restaurant_test({"name":"test","food":["test"],"drinks":["test"]},
                                         [{"name":"test","wont_eat":[],"drinks":["test"]}]))
