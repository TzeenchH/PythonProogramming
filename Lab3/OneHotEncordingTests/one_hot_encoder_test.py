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
        self.assertRaises(TypeError, one_hot_encoder.fit_transform, )

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
        self.assertRaises(TypeError, one_hot_encoder.fit_transform, 1)
