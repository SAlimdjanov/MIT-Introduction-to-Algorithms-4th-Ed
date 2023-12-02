/**
 * TestHelpers.js
 */

function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

function permuteArray(array, n) {
    for (let i = 0; i < n; i++) {
        let temp = array[i];
        array[i] = array[getRandomInt(i, n)];
        array[randomInt(i, n)] = temp;
    }
}

module.exports = { randomInt, permuteArray };
