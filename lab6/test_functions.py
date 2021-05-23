import functions
import pytest


def test_ilen_ok():
    result = functions.ilen((item for item in range(20)))
    assert 20 == result


def test_flatten_ok():
    result = list(functions.flatten([1, [2, 3, [4, 5]]]))
    assert [1, 2, 3, 4, 5] == result


def test_flatten_non_iterable_return_error():
    with pytest.raises(TypeError):
        functions.flatten()


def test_distinct_ok():
    result = list(functions.distinct([1, 2, 3, 0, 0, 4, 4]))
    assert [1, 2, 3, 0, 4] == result


def test_groupby_ok():
    data = [{'gender': 'female', 'age': 23},
            {'gender': 'male', 'age': 20},
            {'gender': 'female', 'age': 21}]
    result = functions.groupby(data, 'gender')
    assert result == {
        'female': [
            {'gender': 'female', 'age': 23},
            {'gender': 'female', 'age': 21}
        ],
        'male': [
            {'gender': 'male', 'age': 20}
        ]
    }


def test_groupby_invalid_key_error():
    gender = [{'gender': 'female', 'age': 23},
              {'gender': 'male', 'age': 20}]
    with pytest.raises(KeyError):
        functions.groupby(gender, 'bender')


def test_groupby_key_is_null_error():
    with pytest.raises(TypeError):
        functions.groupby()


def test_groupby_coll_is_not_iterable_index_error():
    with pytest.raises(IndexError):
        functions.groupby("test", 1)


def test_chunks_ok():
    result = list(functions.chunks([1, 2, 3, 4, 5, 6], 2))
    assert [(1, 2), (3, 4), (5, 6)] == result


def test_chunks_zero_chunk_size_raise_error():
    with pytest.raises(ValueError):
        next(functions.chunks([1, 2, 3], -1))


def test_chunks_invalid_size_raise_error():
    with pytest.raises(TypeError):
        next(functions.chunks([1, 2, 3], 'not int'))


@pytest.mark.parametrize('actual, expected',
                         [
                          (['first', 'second'], 'first'),
                          ('string', 's')
                         ])
def test_first_ok(actual, expected):
    result = functions.first(['first', 'second'])
    assert functions.first(actual) == expected


def test_last_ok():
    result = functions.last(['first', 'middle', 'last'])
    assert 'last' == result
