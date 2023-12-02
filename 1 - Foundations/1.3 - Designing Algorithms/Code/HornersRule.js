/**
 * HornersRule.js
 *
 */

function hornersRule(coeff, x) {
    let n = coeff.length;
    let result = 0;

    for (let i = n - 1; i > -1; i--) {
        result = coeff[i] + x * result;
    }

    return result;
}

module.exports = hornersRule;
