/**
 * LinearTimeSort.test.js
 *
 */

let countingSort = require("../CountingSort");
let bucketSort = require("../BucketSort");

const randomNumber = () => {
    // Random number generator for tests
    return Math.floor(Math.random() * 9) + 1;
};

test("countingSort on a known input array", () => {
    let array = [0, 2, 7, 3, 4, 6, 5, 1, 8];
    let expectedResult = [0, 1, 2, 3, 4, 5, 6, 7, 8];

    expect(countingSort(array, array.length, Math.max(...array))).toStrictEqual(
        expectedResult
    );
});

test("countingSort with a known array containing duplicates", () => {
    let duplicateArray = [6, 0, 2, 0, 1, 3, 4, 6, 3, 1, 2];
    let expectedResult = [0, 0, 1, 1, 2, 2, 3, 3, 4, 6, 6];

    expect(
        countingSort(
            duplicateArray,
            duplicateArray.length,
            Math.max(...duplicateArray)
        )
    ).toStrictEqual(expectedResult);
});

test("countingSort on a randomly generated array", () => {
    let array = Array.from({ length: randomNumber() }, () => randomNumber());
    let expectedResult = [...array].sort();

    expect(countingSort(array, array.length, Math.max(...array))).toStrictEqual(
        expectedResult
    );
});

test("Bucket sort on a known input distribution", () => {
    let array = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21];
    let expectedResult = array.sort();

    expect(bucketSort(array, array.length)).toStrictEqual(expectedResult);
});

test("Bucket Sort on a randomly generated uniform distribution", () => {
    const randomLength = randomNumber();
    let array = Array.from({ length: randomLength }, () => Math.random());
    let expectedResult = [...array].sort();

    expect(bucketSort(array, array.length)).toStrictEqual(expectedResult);
});
