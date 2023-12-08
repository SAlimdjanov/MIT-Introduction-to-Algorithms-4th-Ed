/**
 * DoublyLinkedList.test.js
 *
 */

const DoublyLinkedList = require("../DoublyLinkedList");

const testList = new DoublyLinkedList();

const printList = () => {
    let current = testList.head;
    let currKey = testList.head.key;
    let currPrev = null;
    let currNext = null;

    for (let i = 0; i < testList.size; i++) {
        currKey = current.key;

        if (current.prev) {
            currPrev = current.prev.key;
        } else {
            currPrev = null;
        }

        if (current.next) {
            currNext = current.next.key;
        } else {
            currNext = null;
        }

        console.log(`Prev: ${currPrev}, Key: ${currKey}, Next: ${currNext}`);
        current = current.next;
    }
};

test("Attempting the delete from an empty list throws an error", () => {
    expect(() => {
        testList.llDelete(5);
    }).toThrow(new RangeError("Linked list is empty"));
});

test("Attempting the search an empty list throws an error", () => {
    expect(() => {
        testList.llSearch(5);
    }).toThrow(new ReferenceError("Object with key '5' was not found"));
});

test("Appending to a list behaves properly", () => {
    testList.llAppend(27);

    expect(testList.size).toStrictEqual(1);
    expect(testList.head.key).toStrictEqual(27);
    expect(testList.head.prev).toStrictEqual(null);
    expect(testList.head.next).toStrictEqual(null);
});

test("Prepending to a list behaves properly", () => {
    testList.llPrepend(13);

    expect(testList.size).toStrictEqual(2);
    expect(testList.head.key).toStrictEqual(13);
    expect(testList.head.next.key).toStrictEqual(27);
    expect(testList.head.prev).toStrictEqual(null);
});

test("Deleting the head of the list performs correctly", () => {
    testList.llDelete(testList.head.key);

    expect(testList.size).toStrictEqual(1);
    expect(testList.head.key).toStrictEqual(27);
    expect(testList.head.next).toStrictEqual(null);
    expect(testList.head.prev).toStrictEqual(null);
});

test("Inserting before an object behaves correctly", () => {
    testList.llPrepend(21);
    testList.llInsertBefore(27, 99);

    expect(testList.size).toStrictEqual(3);
    expect(testList.head.key).toStrictEqual(21);
    expect(testList.head.next.key).toStrictEqual(99);
    expect(testList.head.next.prev.key).toStrictEqual(21);
    expect(testList.head.next.next.key).toStrictEqual(27);
});

test("Search for an undefined object throws an error", () => {
    expect(() => testList.llSearch(95)).toThrow(
        new ReferenceError("Object with key '95' was not found")
    );
});

test("Search for an object in the list works properly", () => {
    let result = testList.llSearch(99);
    expect(result.key).toStrictEqual(99);
});

test("Inserting after an object behaves correctly", () => {
    testList.llInsertAfter(99, 56);

    expect(testList.size).toStrictEqual(4);
    expect(testList.llSearch(56).next.key).toStrictEqual(27);
    expect(testList.llSearch(56).prev.key).toStrictEqual(99);
});
