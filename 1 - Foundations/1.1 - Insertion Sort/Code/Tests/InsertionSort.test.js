/**
 * InsertionSort.test.js
 *
 */

const {
    insertionSort,
    insertionSortReversed,
    binaryArrayAddition,
} = require("../InsertionSort");

const inputSequence = [5, 2, 4, 6, 1, 3];
const binA = [1, 0, 1, 0];
const binB = [1, 1, 1, 1];

test("Insertion sort sorts correctly", () => {
    let result = insertionSort(inputSequence, inputSequence.length);

    const expectedResult = [...inputSequence];
    expectedResult.sort((a, b) => a - b);

    expect(result).toStrictEqual(expectedResult);
});

test("Reversed insertion sort sorts correctly", () => {
    let result = insertionSortReversed(inputSequence, inputSequence.length);

    const expectedResult = [...inputSequence];
    expectedResult.sort((a, b) => b - a);

    expect(result).toStrictEqual(expectedResult);
});

test("Binary array addition produces the correct answer", () => {
    let result = binaryArrayAddition(binA, binB, binA.length);
    const expectedResult = [1, 1, 0, 0, 1];

    expect(result).toStrictEqual(expectedResult);
});
