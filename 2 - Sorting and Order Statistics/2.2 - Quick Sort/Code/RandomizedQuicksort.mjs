/**
 * RandomizedQuicksort.mjs
 *
 */

import Quicksort from "./Quicksort.mjs";

export default class RandomizedQuicksort extends Quicksort {
    constructor(array) {
        super(array);
    }

    randomizedPartition(p, r) {
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

    randomizedQuicksort(p, r) {
        if (p < r) {
            let q = this.partition(p, r);
            this.randomizedQuicksort(p, q - 1);
            this.randomizedQuicksort(q + 1, r);
        }
    }
}

const main = () => {
    let array = [2, 8, 7, 1, 10, 5, 6, 4, 9, 3];
    let p = 0;
    let r = array.length - 1;

    let randomSort = new RandomizedQuicksort(array);
    randomSort.randomizedQuicksort(p, r);

    console.log(randomSort.array);
};

main();
