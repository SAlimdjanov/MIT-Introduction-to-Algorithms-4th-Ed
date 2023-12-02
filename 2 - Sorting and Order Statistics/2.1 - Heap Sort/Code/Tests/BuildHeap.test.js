/**
 * BuildHeap.test.js
 *
 */

const BuildHeap = require("../BuildHeap");
const { isMinHeap, isMaxHeap } = require("./TestHelpers");

const array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7];

test("buildMaxHeap produces a valid max-heap", () => {
    let maxHeap = new BuildHeap(array);
    maxHeap.buildMaxHeap();

    expect(isMaxHeap(maxHeap.heap)).toBe(true);
});

test("buildMaxHeap produces a valid max-heap", () => {
    let minHeap = new BuildHeap(array);
    minHeap.buildMinHeap();

    expect(isMinHeap(minHeap.heap)).toBe(true);
});
