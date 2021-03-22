import unittest
import one_hot_encoder


class TestOneHotEncoder(unittest.TestCase):
    def test_execute_four_cities_success(self):
        cities = ['Moscow', 'New York', 'Berlin', 'London']
        expected = [
            ('Moscow', [0, 0, 0, 1]),
            ('New York', [0, 0, 1, 0]),
            ('Berlin', [0, 1, 0, 0]),
            ('London', [1, 0, 0, 0]),
        ]
        actual = one_hot_encoder.fit_transform(cities)
        self.assertEqual(actual, expected)

    def test_execute_zero_args_typeerror(self):
        cities = []
        result = one_hot_encoder.fit_transform(cities)
        self.assertRaises(TypeError, result)

    def test_execute_same_cities_tuple(self):
        cities = ['Tokyo', 'Tokyo', 'Tokyo']
        expected = [
            ('Tokyo', [1]),
            ('Tokyo', [1]),
            ('Tokyo', [1]),
        ]
        actual = one_hot_encoder.fit_transform(cities)
        self.assertEqual(actual, expected)

    def test_execute_four_cities_no_unexpected_indexes(self):
        cities = ['Moscow', 'New York', 'Berlin', 'London']
        actual = one_hot_encoder.fit_transform(cities)
        self.assertIsNotNone(actual)
        self.assertNotIn(('Moscow', [1, 0, 0, 0]), actual)
