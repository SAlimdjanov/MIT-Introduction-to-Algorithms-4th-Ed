/**
 * DirectAddressTable.js
 *
 */

class TableObject {
    constructor(key, data) {
        this.key = key;
        this.data = data;
    }
}

class DirectAddressTable {
    constructor() {
        this.table = new Map();
    }

    search(k) {
        return this.table.get(k);
    }

    insert(x) {
        this.table.set(x.key, x);
    }

    delete(x) {
        this.table.set(x.key, null);
    }
}

module.exports = { TableObject, DirectAddressTable };
