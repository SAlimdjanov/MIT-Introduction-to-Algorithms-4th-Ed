"""
test_direct_address_table.py

"""


from ..direct_address_table import TableObject, DirectAddressTable


object_1 = TableObject(2, "Hello")
object_2 = TableObject(15, "World")
test_table = DirectAddressTable()


def test_insert():
    """An object can be inserted into the table"""
    test_table.insert(object_1)
    test_table.insert(object_2)

    assert (
        test_table.table[object_1.key].key == 2
        and test_table.table[object_1.key].data == "Hello"
        and test_table.table[object_2.key].key == 15
        and test_table.table[object_2.key].data == "World"
    )


def test_search():
    """An object can be found"""
    result = test_table.search(2)

    assert result.key == 2 and result.data == "Hello"


def test_delete():
    """An object can be deleted"""
    test_table.delete(object_2)

    assert test_table.table[15] is None
