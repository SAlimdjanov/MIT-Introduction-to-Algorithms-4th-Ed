/**
 * Queue.test.js
 *
 */

const Queue = require("../Queue");

const testQueue = new Queue(5);

test("Attempting to dequeue an empty queue throws an error", () => {
    expect(() => {
        testQueue.dequeue();
    }).toThrow(new RangeError("Queue is empty"));
});

test("Attempting to enqueue a full queue throws an error", () => {
    for (let i = 0; i < testQueue.size; i++) {
        testQueue.enqueue(i);
    }

    expect(() => {
        testQueue.enqueue();
    }).toThrow(new RangeError("Queue is full"));
});

test("Dequeuing the first two element obtains the correct results", () => {
    let tails = new Array();
    let dequeued = new Array();

    for (let i = 0; i < 2; i++) {
        dequeued.push(testQueue.dequeue());
        tails.push(testQueue.tail);
    }

    expect(tails).toStrictEqual([4, 3]);
    expect(dequeued).toStrictEqual([0, 1]);
    expect(testQueue.queue).toStrictEqual([2, 3, 4, NaN, NaN]);
});

test("Enqueuing an element behaves correctly", () => {
    testQueue.enqueue(55);

    expect(testQueue.queue).toStrictEqual([2, 3, 4, 55, NaN]);
});
