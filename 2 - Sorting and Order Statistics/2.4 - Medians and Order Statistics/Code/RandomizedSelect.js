/**
 * RandomizedSelect.js
 *
 */

class RandomizedSelect {
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

    randomizedPartition(p, r) {
        let i = Math.floor(Math.random() * (r - p) + p);

        let temp = this.array[r];
        this.array[r] = this.array[i];
        this.array[i] = temp;

        return this.partition(p, r);
    }

    randomizedSelect(p, r, i) {
        if (p == r) {
            return this.array[p];
        }

        let q = this.randomizedPartition(p, r);
        let k = q - p + 1;

        if (i == k) {
            return this.array[q];
        }

        if (i < k) {
            return this.randomizedSelect(p, q - 1, i);
        }

        return this.randomizedSelect(q + 1, r, i - k);
    }
}

module.exports = RandomizedSelect;
