"""
test_doubly_linked_list.py

"""


from pytest import raises
from ..doubly_linked_list import DoublyLinkedList


test_list = DoublyLinkedList()


def test_empty_delete():
    """Deleting from an empty list throws a KeyError"""
    with raises(KeyError, match="Linked list is empty"):
        test_list.ll_delete(5)


def test_empty_search():
    """Searching an empty list throws a KeyError"""
    with raises(KeyError, match="Object with key '5' was not found in the list"):
        test_list.ll_search(5)


def test_list_append():
    """Appending to an empty list behaves properly"""
    test_list.ll_append(27)

    assert (
        test_list.length == 1
        and test_list.head.key == 27
        and test_list.head.next is None
        and test_list.head.prev is None
    )


def test_list_prepend():
    """Prepending to the list results in the correct element key showing at the head"""
    test_list.ll_prepend(13)

    assert (
        test_list.length == 2
        and test_list.head.key == 13
        and test_list.head.next.key == 27
        and test_list.head.prev is None
    )


def test_list_delete_head():
    """Deleting the head of the list performs correctly"""
    test_list.ll_delete(test_list.head.key)

    assert (
        test_list.length == 1
        and test_list.head.key == 27
        and test_list.head.next is None
        and test_list.head.prev is None
    )


def test_list_insert_before():
    """Inserting before an object behaves appropriately"""
    test_list.ll_prepend(21)
    test_list.ll_insert_before(k=27, k_new=99)

    assert (
        test_list.length == 3
        and test_list.head.key == 21
        and test_list.head.next.key == 99
        and test_list.head.next.prev.key == 21
        and test_list.head.next.next.key == 27
    )


def test_list_search():
    """Search for an object of a defined key returns the object correctly"""
    result = test_list.ll_search(99)

    assert result.key == 99


def test_list_search_undefined():
    """Search for an object of an undefined key throws an error"""
    with raises(KeyError, match="Object with key '95' was not found in the list"):
        test_list.ll_search(95)


def test_list_insert_after():
    """Inserting before an object behaves appropriately"""
    test_list.ll_insert_after(k=99, k_new=56)

    assert (
        test_list.length == 4
        and test_list.ll_search(56).next.key == 27
        and test_list.ll_search(56).prev.key == 99
    )
