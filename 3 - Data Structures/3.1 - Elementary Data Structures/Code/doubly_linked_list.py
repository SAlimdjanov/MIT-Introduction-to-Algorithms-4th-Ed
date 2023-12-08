"""
doubly_linked_list.py

"""


class DoublyLinkedList:
    """Doubly Linked List without sentinels. This extends the baseline functionality presented in
    the book"""

    class ListObject:
        """Initializes a linked list object of key value 'key (int)'"""

        def __init__(self, key):
            self.key = key
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.length = 0

    def ll_append(self, k):
        """Append an element to the back of the list

        Args:
            k (int): Value of the key of the new element
        """
        new_obj = self.ListObject(k)

        if self.head is None:
            new_obj.prev = None
            self.head = new_obj
        else:
            current_obj = self.head

            while current_obj.next:
                current_obj = current_obj.next

            current_obj.next = new_obj
            new_obj.prev = current_obj
            new_obj.next = None

        self.length += 1

    def ll_prepend(self, k):
        """Insert a ListObject to the front of the linked list

        Args:
            k (int): Key of the object to be added to the list
        """
        new_obj = self.ListObject(k)

        if self.head is None:
            new_obj.prev = None
            self.head = new_obj
        else:
            self.head.prev = new_obj
            new_obj.next = self.head
            self.head = new_obj
            new_obj.prev = None

        self.length += 1

    def ll_insert_after(self, k, k_new):
        """Insert an element with key 'k_new' into the list after an element of key 'k'

        Args:
            k (int): Key of the object that you want to insert an object after
            k_new (int): Key value of the new object
        """
        current_obj = self.head
        new_obj = self.ListObject(k_new)

        while current_obj:
            if current_obj.next is None and current_obj.key == k:
                self.ll_append(k_new)
            elif current_obj.key == k:
                next_obj = current_obj.next
                current_obj.next = new_obj
                new_obj.next = next_obj
                new_obj.prev = current_obj
                next_obj.prev = new_obj

            current_obj = current_obj.next

        self.length += 1

    def ll_insert_before(self, k, k_new):
        """Insert an element with key 'k_new' into the list before an element of key 'k'

        Args:
            k (int): Key of the object that you want to insert an object before
            k_new (int): Key value of the new object
        """
        current_obj = self.head
        new_obj = self.ListObject(k_new)

        while current_obj:
            if current_obj.prev is None and current_obj.key == k:
                self.ll_prepend(k_new)
            elif current_obj.key == k:
                prev_obj = current_obj.prev
                prev_obj.next = new_obj
                current_obj.prev = new_obj
                new_obj.next = current_obj
                new_obj.prev = prev_obj

            current_obj = current_obj.next

        self.length += 1

    def ll_search(self, k):
        """Search for an object in the list. Throws a KeyError if not found.

        Args:
            k (int): Key associated with the object

        Returns:
            ListObject: The object associated with the key
        """
        obj = self.head

        while obj is not None and obj.key != k:
            obj = obj.next

        if obj is None:
            raise KeyError(f"Object with key '{k}' was not found in the list")

        return obj

    def ll_delete(self, k):
        """Deletes an element from the list. Throws a KeyError if not found.

        Args:
            k (int): Key of the object to delete
        """
        if self.length == 0:
            raise KeyError("Linked list is empty")

        obj = self.ll_search(k)

        if obj.prev is not None:
            obj.prev.next = obj.next
        else:
            self.head = obj.next

        if obj.next is not None:
            obj.next.prev = obj.prev

        self.length -= 1
