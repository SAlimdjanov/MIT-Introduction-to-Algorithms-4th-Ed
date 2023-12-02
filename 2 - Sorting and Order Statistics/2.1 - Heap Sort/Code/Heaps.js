/**
 * Heaps.mjs
 *
 */

class Heap {
    constructor(heap) {
        this.heap = heap;
    }

    parent(index) {
        let result = Math.floor((index - 1) / 2);

        if (result === -1) {
            return 0;
        }

        return result;
    }

    leftChild(index) {
        return 2 * index + 1;
    }

    rightChild(index) {
        return 2 * (index + 1);
    }
}

module.exports = Heap;
