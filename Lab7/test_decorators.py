import decorators


def test_potentially_unsafe_ok():
    result = decorators.potentially_unsafe_func('name')
    assert 'test' == result


def test_sum_of_values_ok():
    result = decorators.sum_of_two([1, 2])
    assert result == 3


def test_universal_sum_ok():
    result = decorators.universal_sum([1, 2, 3])


def test_universal_length_ok():
    result = decorators.universal_msg("test")
    assert result == "universal message was: test"


def test_length_ok():
    result = decorators.some_msg("lorem ipsum")
    assert result == "Message was: lorem ipsum"


def test_process_text_ok():
    result = decorators.process_text('the French revolution resulted in 3 concepts:freedom,equality,fraternity')
    assert result == 'ThE FrencH RevolutioN ResulteD IN 3 ConceptS FreedoM EqualitY FraternitY'


def test_another_process_text_ok():
    result = decorators.another_process('the French revolution resulted in 3 concepts:freedom,equality,fraternity')
    assert result == 'ThE FrencH RevolutioN ResulteD IN 3 Concepts Freedom Equality FraternitY'