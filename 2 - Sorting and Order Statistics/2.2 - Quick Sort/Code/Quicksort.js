/**
 * Quicksort.js
 *
 */

class Quicksort {
    constructor(array) {
        this.array = array;
    }

    partition(p, r) {
        let x = this.array[r];
        let i = p - 1;

        for (let j = p; j < r; j++) {
            if (this.array[j] <= x) {
                i += 1;
                let temp = this.array[i];
                this.array[i] = this.array[j];
                this.array[j] = temp;
            }
        }

        let temp = this.array[i + 1];
        this.array[i + 1] = this.array[r];
        this.array[r] = temp;

        return i + 1;
    }

    quicksort(p, r) {
        if (p < r) {
            let q = this.partition(p, r);
            this.quicksort(p, q - 1);
            this.quicksort(q + 1, r);
        }
    }
}

module.exports = Quicksort;
