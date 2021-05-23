from typing import Iterable, Any


def ilen(coll: Iterable) -> int:
    """
    Функция получения размера генератора
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    return len(list(coll))


def flatten(mas: Iterable[Any]) -> Iterable[Any]:
    """
    Функция, которая из многоуровневого массива делает одноуровневый
    >>> list(flatten([1, [2, [3, 4]]]))
    [1, 2, 3, 4]
    """
    for item in mas:
        if isinstance(item, (list, tuple, set)):
            yield from flatten(item)
        elif isinstance(item, (int, str, float, bool)):
            yield item
        else:
            raise ValueError("unexpected type token")


def distinct(coll: Iterable):
    """
    Функция, которая удаляет дубликаты с сохранением порядка
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    mas = []
    for i in coll:
        if i not in mas:
            mas.append(i)
            yield i


def groupby(coll: Iterable, key):
    """
        Функция которая собирает словарь из неупорядоченной последовательности словарей, сгруппированных по ключу
       >>> users = [ {'gender': 'female', 'age': 33}, {'gender': 'male', 'age': 20}, {'gender': 'female', 'age': 21}]
       >>> groupby(users, 'gender')
       {'female': [{'gender': 'female', 'age': 33}, {'gender': 'female', 'age': 21}], 'male': [{'gender': 'male', 'age': 20}]}
       """
    tmp = {}
    for item in coll:
        if item[key] not in tmp:
            tmp[item[key]] = []
        tmp[item[key]].append(item)
    return tmp


def chunks(coll: Iterable, size: int) -> Iterable[Any]:
    """
        Функция, которая разбивает последовательность на заданные куски
        >>> list(chunks([0, 1, 2, 3, 4], 3))
        [(0, 1, 2), (3, 4, None)]
        """
    if not isinstance(size, int):
        raise TypeError()
    if size <= 0:
        raise ValueError()

    tmp = []
    for item in coll:
        tmp.append(item)
        if len(tmp) == size:
            yield tuple(tmp)
            tmp = []
    if len(tmp) > 0:
        tmp.append(None)
        yield tuple(tmp)


def first(coll: Iterable) -> Any:
    """
    Функция получения первого элемента или None
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> print(first(range(0)))
    None
    """
    return next(iter(coll), None)


def last(coll: Iterable) -> Any:
    """
    Функция получения последнего элемента или None
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> print(last(range(0)))
    None
    """
    counter = None
    for counter in coll:
        pass
    return counter
