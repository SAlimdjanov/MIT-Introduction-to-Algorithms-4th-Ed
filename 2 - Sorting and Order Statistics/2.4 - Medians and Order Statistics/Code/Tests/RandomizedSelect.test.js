/**
 * RandomizedSelect.test.js
 *
 */

const RandomizedSelect = require("../RandomizedSelect");

const array = [6, 19, 4, 12, 14, 9, 15, 7, 8, 11, 3, 13, 2, 5];
let orderStatistic = new RandomizedSelect(array);
const P = 0;
const R = array.length - 1;
const I = 5;

test("randomizedSelect picks the correct order statistic", () => {
    expect(orderStatistic.randomizedSelect(P, R, I)).toStrictEqual(6);
});
