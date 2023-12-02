/**
 * MatrixMultiply.test.js
 *
 */

const {
    matrixMultiplyIterative,
    matrixMultiplyRecursive,
} = require("../MatrixMultiply");

// Matrices

const matrixA = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15],
];

const matrixB = [
    [16, 17, 18, 19],
    [20, 21, 22, 23],
    [24, 25, 26, 27],
    [28, 29, 30, 31],
];

const matrixC = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
];

// Solution

const answer = [
    [152, 158, 164, 170],
    [504, 526, 548, 570],
    [856, 894, 932, 970],
    [1208, 1262, 1316, 1370],
];

// Tests

test("Iterative function produces the correct answer", () => {
    matrixMultiplyIterative(matrixA, matrixB, matrixC, matrixC.length);
    expect(matrixC).toStrictEqual(answer);
});

test("Recursive function produces the correct answer", () => {
    let newMatrixC = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ];

    matrixMultiplyRecursive(matrixA, matrixB, newMatrixC, newMatrixC.length);

    expect(newMatrixC).toStrictEqual(answer);
});
