let countingSort = require("../CountingSort");
let bucketSort = require("../BucketSort");

test("countingSort", () => {
    let array = [0, 2, 7, 3, 4, 6, 5, 1, 8];
    let expectedResult = [0, 1, 2, 3, 4, 5, 6, 7, 8];

    expect(countingSort(array, array.length, Math.max(...array))).toStrictEqual(
        expectedResult
    );
});

test("countingSort with duplicates", () => {
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

test("Bucket Sort on a randomly generated uniform distribution", () => {
    let array = [];
    for (let i = 0; i < 10; i++) {
        array.push(Math.random());
    }

    let expectedResult = [...array].sort();

    expect(bucketSort(array, array.length)).toStrictEqual(expectedResult);
});
