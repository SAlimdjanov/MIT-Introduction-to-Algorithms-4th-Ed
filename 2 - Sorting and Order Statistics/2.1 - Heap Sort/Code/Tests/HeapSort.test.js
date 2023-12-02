/**
 * HeapSort.test.js
 *
 */

const HeapSort = require("../HeapSort");

// Min and Max heaps
const maxHeap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1];
const minHeap = [...maxHeap];
minHeap.reverse();

test("heapSort should sort a max-heap correctly", () => {
    let sortMax = new HeapSort(maxHeap);
    sortMax.heapSort();

    let expectedResult = [...maxHeap];
    expectedResult.sort((a, b) => a - b);

    expect(sortMax.heap).toStrictEqual(expectedResult);
});

test("heapSort should sort a min-heap correctly", () => {
    let sortMin = new HeapSort(minHeap);
    sortMin.heapSort();

    let expectedResult = [...minHeap];
    expectedResult.sort((a, b) => a - b);

    expect(sortMin.heap).toStrictEqual(expectedResult);
});
