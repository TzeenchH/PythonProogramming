import pytest
import one_hot_encoder


def test_cities_tuple_success():
    cities = ['Moscow', 'New York', 'Berlin', 'London']
    expected = [
        ('Moscow', [0, 0, 0, 1]),
        ('New York', [0, 0, 1, 0]),
        ('Berlin', [0, 1, 0, 0]),
        ('London', [1, 0, 0, 0]),
    ]
    actual = one_hot_encoder.fit_transform(cities)
    assert actual == expected


def test_empty_tuple_raise_error():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform()


def test_same_cities_tuple_success():
    cities = ['Tokyo', 'Tokyo', 'Tokyo']
    expected = [
        ('Tokyo', [1]),
        ('Tokyo', [1]),
        ('Tokyo', [1]),
    ]
    actual = one_hot_encoder.fit_transform(cities)
    assert actual == expected


def test_tuple_has_value_success():
    cities = ['Tokyo', 'Tokyo', 'Tokyo']
    actual = one_hot_encoder.fit_transform(cities)
    assert actual is not None
