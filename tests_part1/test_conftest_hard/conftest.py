import pytest


@pytest.fixture
def list_creator(incoming_list):
    return list(map(int, incoming_list))
