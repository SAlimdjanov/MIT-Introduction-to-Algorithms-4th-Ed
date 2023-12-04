/**
 * MinAndMax.js
 *
 */

class MinAndMax {
    constructor(array) {
        this.array = array;
        this.n = array.length;
    }

    minimum() {
        let minVal = this.array[0];

        for (let i = 1; i < this.n; i++) {
            if (minVal > this.array[i]) {
                minVal = this.array[i];
            }
        }

        return minVal;
    }

    maximum() {
        let maxVal = this.array[0];

        for (let i = 1; i < this.n; i++) {
            if (maxVal < this.array[i]) {
                maxVal = this.array[i];
            }
        }

        return maxVal;
    }
}

module.exports = MinAndMax;
