# фаил c тестами № 2
# Основной текст задания находится в файле main_summer_test.py
#
from functools import reduce

import pytest


# Исходная функция:
def multiplicator(*args):
    return reduce(lambda x, y: x*y, args)


@pytest.fixture
def incoming_list():
    return [1, "2", 10, "20", 1, 5, 3 ,8]


def test_multiplicator(list_creator):
    list_mult = reduce(lambda x, y: x*y, list_creator)
    assert multiplicator(*list_creator) == list_mult
