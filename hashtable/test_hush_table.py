from hash_table import HashTable, LinkedList, _Node

import pytest

@pytest.fixture
def test_hash_table():
    hash_table = HashTable(1024)

    hash_table.add("Guitar", "Gibson")
    hash_table.add("Bass", "Fender")
    hash_table.add("symbol", "Zildjan")
    hash_table.add("car", "tesla")
    hash_table.add("NewKey", "new value")
    hash_table.add(10, "int key")
    hash_table.add(0.5, "float key")

    return hash_table


def test_create_hash_table_5elements():

    hash_table = HashTable(5)

    assert hash_table.array == [0, 0, 0, 0, 0]


def test_hash_method():
    hash_table = HashTable(1024)

    assert hash_table.hash('Guitar') == 692

    assert hash_table.hash("piano") == 977
