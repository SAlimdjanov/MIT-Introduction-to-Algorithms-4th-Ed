/**
 * DoublyLinkedList.js
 *
 */

class ListObject {
    constructor(key) {
        this.key = key;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }

    llPrepend(k) {
        let newObject = new ListObject(k);

        if (this.head === null) {
            newObject.prev = null;
            this.head = newObject;
        } else {
            this.head.prev = newObject;
            newObject.next = this.head;
            this.head = newObject;
            newObject.prev = null;
        }

        this.size += 1;
    }

    llAppend(k) {
        let newObject = new ListObject(k);

        if (this.head === null) {
            newObject.prev = null;
            this.head = newObject;
        } else {
            let currentObject = this.head;

            while (currentObject.next) {
                currentObject = currentObject.next;
            }

            currentObject.next = newObject;
            newObject.prev = currentObject;
            newObject.next = null;
        }

        this.size += 1;
    }

    llInsertAfter(k, kNew) {
        let currentObject = this.head;
        let newObject = new ListObject(kNew);

        while (currentObject) {
            if (currentObject.next === null && currentObject.key === k) {
                this.llAppend(kNew);
            } else if (currentObject.key === k) {
                let nextObject = currentObject.next;
                currentObject.next = newObject;
                newObject.next = nextObject;
                newObject.prev = currentObject;
                nextObject.prev = newObject;
            }

            currentObject = currentObject.next;
        }

        this.size += 1;
    }

    llInsertBefore(k, kNew) {
        let currentObject = this.head;
        let newObject = new ListObject(kNew);

        while (currentObject) {
            if (currentObject.prev === null && currentObject.key === k) {
                this.llAppend(kNew);
            } else if (currentObject.key === k) {
                let previousObject = currentObject.prev;
                previousObject.next = newObject;
                currentObject.prev = newObject;
                newObject.next = currentObject;
                newObject.prev = previousObject;
            }

            currentObject = currentObject.next;
        }

        this.size += 1;
    }

    llSearch(k) {
        let object = this.head;

        while (object != null && object.key != k) {
            object = object.next;
        }

        if (object === null) {
            throw new ReferenceError(`Object with key '${k}' was not found`);
        }

        return object;
    }

    llDelete(k) {
        if (this.size === 0) {
            throw new RangeError("Linked list is empty");
        }

        let object = this.llSearch(k);

        if (object.prev != null) {
            object.prev.next = object.next;
        } else {
            this.head = object.next;
        }

        if (object.next != null) {
            object.next.prev = object.prev;
        }

        this.size -= 1;
    }
}

module.exports = DoublyLinkedList;
