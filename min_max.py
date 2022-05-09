from math import inf
from numbers import Number
from typing import Iterable, Tuple, Iterator


def _min_max_recursive(iterator: Iterator, min_value: Number, max_value: Number):
    try:
        element = next(iterator)
    except StopIteration:
        return min_value, max_value
    else:
        if element < min_value:
            min_value = element
        if element > max_value:
            max_value = element
        return _min_max_recursive(iterator, min_value, max_value)


def min_max(iteravel: Iterable) -> Tuple[Number, Number]:
    """
    >>> min_max([])
    Traceback (most recent call last):
        ...
    ValueError: Não existe mínimo e máximo de iterável sem elemento.

    >>> min_max([1])
    (1, 1)

    >>> min_max(range(800))
    (0, 799)


    :param iteravel:
    :return:
    """
    iterator = iter(iteravel)
    min_value, max_value = _min_max_recursive(iterator, inf, -inf)
    if min_value is inf:
        raise ValueError("Não existe mínimo e máximo de iterável sem elemento.")
    return min_value, max_value
