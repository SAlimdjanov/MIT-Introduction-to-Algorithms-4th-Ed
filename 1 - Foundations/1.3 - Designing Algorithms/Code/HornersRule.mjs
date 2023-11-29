/**
 * HornersRule.mjs
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

const main = () => {
    // 1 + 2x + 3x^2 + 4x^4
    let polynomialCoeff = [1, 2, 3, 0, 4];

    let p = hornersRule(polynomialCoeff, 5);
    console.log(p);
};

// main();

export default hornersRule;
