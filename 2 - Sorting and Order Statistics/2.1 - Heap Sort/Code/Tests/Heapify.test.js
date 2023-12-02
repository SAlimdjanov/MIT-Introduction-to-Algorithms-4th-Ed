/**
 * Heapify.test.js
 *
 */

const Heapify = require("../Heapify");
const { isMinHeap, isMaxHeap } = require("./TestHelpers");

test("maxHeapify should produce a valid max-heap", () => {
    const maxArray = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1];
    let heapifyMax = new Heapify(maxArray);
    heapifyMax.maxHeapify(1);

    expect(isMaxHeap(heapifyMax.heap)).toBe(true);
});

test("minHeapify should produce a valid min-heap", () => {
    const minArray = [1, 3, 14, 4, 7, 8, 9, 2, 10, 16];
    let heapifyMin = new Heapify(minArray);
    heapifyMin.minHeapify(2);

    expect(isMinHeap(heapifyMin.heap)).toBe(true);
});
