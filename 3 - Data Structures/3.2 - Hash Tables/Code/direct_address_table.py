"""
direct_address_table.py

"""


class TableObject:
    """Table object"""

    def __init__(self, key, data):
        """Constructs an object containing a key and satellite data

        Args:
            key (int): Element Key
            data (any): Satellite data
        """
        self.key = key
        self.data = data


class DirectAddressTable:
    """Implements a Direct Address Table in O(1) time and space complexity"""

    def __init__(self):
        self.table = {}

    def search(self, k):
        """Search for an object in the table

        Args:
            k (int): Search key

        Returns:
            TableObject: Object associated with the key
        """
        return self.table[k]

    def insert(self, x):
        """Insert an object into the table

        Args:
            x (TableObject): Table object to be inserted
        """
        self.table[x.key] = x

    def delete(self, x):
        """Deletes a list object by setting its table reference to 'None'

        Args:
            x (TableObject): Table object to be deleted
        """
        self.table[x.key] = None
