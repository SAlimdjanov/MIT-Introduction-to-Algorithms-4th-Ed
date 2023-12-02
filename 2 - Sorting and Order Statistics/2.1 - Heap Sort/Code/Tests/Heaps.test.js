/**
 * Heaps.test.js
 *
 */

const Heap = require("../Heaps");

// Max Heap

const heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1];
let heapNodes = new Heap(heap);
let heapLength = heap.length;

// Expected values (Compliant Max Heap)

const expParents = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4];

const expLeftChildren = () => {
    let results = [];
    for (let i = 0; i < heapLength; i++) {
        results.push(2 * i + 1);
    }
    return results;
};

const expRightChildren = () => {
    let results = [];
    for (let i = 0; i < heapLength; i++) {
        results.push(2 * i + 2);
    }
    return results;
};

// Generate results for Heap methods

const generateResults = (funct) => {
    let results = [];
    for (let i = 0; i < heapLength; i++) {
        results.push(funct(i));
    }
    return results;
};

test("Heap parent method works correctly", () => {
    let results = generateResults(heapNodes.parent);
    expect(results).toStrictEqual(expParents);
});

test("Heap leftChild method works correctly", () => {
    let results = generateResults(heapNodes.leftChild);
    expect(results).toStrictEqual(expLeftChildren());
});

test("Heap rightChild method works correctly", () => {
    let results = generateResults(heapNodes.rightChild);
    expect(results).toStrictEqual(expRightChildren());
});
