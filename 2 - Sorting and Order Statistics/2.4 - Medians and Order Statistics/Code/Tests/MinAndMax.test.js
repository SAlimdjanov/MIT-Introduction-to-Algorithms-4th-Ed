/**
 * MinAndMax.test.js
 *
 */

const MinAndMax = require("../MinAndMax");

const array = [1, 8, 3, 4, 6, 5, 2, 7];
let comparison = new MinAndMax(array);

test("Minimum returns the correct minumum", () => {
    expect(Math.min(...array)).toStrictEqual(comparison.minimum());
});

test("Maximum returns the correct maximum", () => {
    expect(Math.max(...array)).toStrictEqual(comparison.maximum());
});
