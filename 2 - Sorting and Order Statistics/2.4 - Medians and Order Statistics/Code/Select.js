/**
 * Select.js
 *
 */

class Select {
    constructor(array) {
        this.array = array;
    }

    partitionAround(p, r, x) {
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

    select(p, r, i) {
        while ((r - p + 1) % 5 != 0) {
            for (let j = p + 1; j < r + 1; j++) {
                if (this.array[p] > this.array[j]) {
                    let temp = this.array[j];
                    this.array[j] = this.array[p];
                    this.array[p] = temp;
                }
            }

            if (i == 1) {
                return this.array[p];
            }

            p += 1;
            i -= 1;
        }

        let g = Math.floor((r - p + 1) / 5);

        for (let j = p; j < p + g; j++) {
            let indices = [j, j + g, j + 2 * g, j + 3 * g, j + 4 * g].filter(
                (index) => index <= r
            );
            let elements = indices.map((index) => this.array[index]);

            elements.sort((a, b) => a - b);

            for (let k = 0; k < indices.length; k++) {
                let index = indices[k];
                let sortedValue = elements[k];
                this.array[index] = sortedValue;
            }
        }

        let x = this.select(p + 2 * g, p + 3 + g - 1, Math.ceil(g / 2));
        let q = this.partitionAround(p, r, x);

        let k = q - p + 1;

        if (i == k) {
            return this.array[q];
        }

        if (i < k) {
            return this.select(p, q - 1, i);
        }

        return this.select(q + 1, r, i - k);
    }
}

module.exports = Select;
