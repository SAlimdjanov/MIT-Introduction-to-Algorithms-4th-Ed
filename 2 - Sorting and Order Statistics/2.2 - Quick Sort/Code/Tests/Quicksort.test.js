/**
 * Quicksort.test.js
 *
 */

let Quicksort = require("../Quicksort");
let RandomizedQuicksort = require("../RandomizedQuicksort");

const randomNumber = () => {
    // Random number generator for tests
    return Math.floor(Math.random() * 9) + 1;
};

test("Quicksort on a known input array", () => {
    let array = [2, 8, 7, 1, 3, 5, 6, 4];
    let expectedResult = [...array].sort();
    let p = 0;
    let r = array.length - 1;

    let sort = new Quicksort(array);
    sort.quicksort(p, r);

    expect(sort.array).toStrictEqual(expectedResult);
});

test("Quicksort on a randomly generated array", () => {
    let array = Array.from({ length: randomNumber() }, () => randomNumber());
    let expectedResult = [...array].sort();
    let p = 0;
    let r = array.length - 1;

    let sort = new Quicksort(array);
    sort.quicksort(p, r);

    expect(sort.array).toStrictEqual(expectedResult);
});

test("Randomized Quicksort on a known input array", () => {
    let array = [2, 8, 7, 1, 3, 5, 6, 4];
    let expectedResult = [...array].sort();
    let p = 0;
    let r = array.length - 1;

    let sort = new RandomizedQuicksort(array);
    sort.randomizedQuicksort(p, r);

    expect(sort.array).toStrictEqual(expectedResult);
});

test("Randomized Quicksort on a randomly generated array", () => {
    let array = Array.from({ length: randomNumber() }, () => randomNumber());
    let expectedResult = [...array].sort();
    let p = 0;
    let r = array.length - 1;

    let sort = new RandomizedQuicksort(array);
    sort.randomizedQuicksort(p, r);

    expect(sort.array).toStrictEqual(expectedResult);
});
