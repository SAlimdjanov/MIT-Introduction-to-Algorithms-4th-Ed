/*
 * MatrixMultiply.js
 *
 */

function matrixMultiplyIterative(A, B, C, n) {
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            for (let k = 0; k < n; k++) {
                C[i][j] = C[i][j] + A[i][k] * B[k][j];
            }
        }
    }
}

function matrixMultiplyRecursive(A, B, C, n) {
    if (n === 1) {
        C[0][0] = C[0][0] + A[0][0] * B[0][0];
        return;
    }

    let a11 = A.slice(0, n / 2).map((row) => row.slice(0, n / 2));
    let a12 = A.slice(0, n / 2).map((row) => row.slice(n / 2));
    let a21 = A.slice(n / 2).map((row) => row.slice(0, n / 2));
    let a22 = A.slice(n / 2).map((row) => row.slice(n / 2));

    let b11 = B.slice(0, n / 2).map((row) => row.slice(0, n / 2));
    let b12 = B.slice(0, n / 2).map((row) => row.slice(n / 2));
    let b21 = B.slice(n / 2).map((row) => row.slice(0, n / 2));
    let b22 = B.slice(n / 2).map((row) => row.slice(n / 2));

    let c11 = C.slice(0, n / 2).map((row) => row.slice(0, n / 2));
    let c12 = C.slice(0, n / 2).map((row) => row.slice(n / 2));
    let c21 = C.slice(n / 2).map((row) => row.slice(0, n / 2));
    let c22 = C.slice(n / 2).map((row) => row.slice(n / 2));

    matrixMultiplyRecursive(a11, b11, c11, n / 2);
    matrixMultiplyRecursive(a12, b21, c11, n / 2);
    matrixMultiplyRecursive(a11, b12, c12, n / 2);
    matrixMultiplyRecursive(a12, b22, c12, n / 2);
    matrixMultiplyRecursive(a21, b11, c21, n / 2);
    matrixMultiplyRecursive(a22, b21, c21, n / 2);
    matrixMultiplyRecursive(a21, b12, c22, n / 2);
    matrixMultiplyRecursive(a22, b22, c22, n / 2);

    for (let i = 0; i < n / 2; i++) {
        for (let j = 0; j < n / 2; j++) {
            C[i][j] = c11[i][j];
            C[i][j + n / 2] = c12[i][j];
            C[i + n / 2][j] = c21[i][j];
            C[i + n / 2][j + n / 2] = c22[i][j];
        }
    }
}

module.exports = { matrixMultiplyIterative, matrixMultiplyRecursive };
