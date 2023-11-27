/**
 * Quicksort.mjs
 *
 */

export default class Quicksort {
    constructor(array) {
        this.array = array;
    }

    partition(p, r) {
        let x = this.array[r];
        let i = p - 1;

        for (var j = p; j < r; j++) {
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

const main = () => {
    let array = [2, 8, 7, 1, 3, 5, 6, 4];
    let p = 0;
    let r = array.length - 1;

    let sort = new Quicksort(array);
    sort.quicksort(p, r);
    console.log(sort.array);
};

// main();
