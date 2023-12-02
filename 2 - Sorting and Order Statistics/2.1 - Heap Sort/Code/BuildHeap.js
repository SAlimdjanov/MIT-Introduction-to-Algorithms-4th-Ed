/**
 * BuildHeap.js
 *
 */

const Heapify = require("./Heapify");

class BuildHeap extends Heapify {
    constructor(heap) {
        super(heap);
    }

    buildMaxHeap() {
        for (let i = Math.floor(this.heapSize / 2); i > -1; i--) {
            this.maxHeapify(i);
        }
    }

    buildMinHeap() {
        for (let i = Math.floor(this.heapSize / 2); i > -1; i--) {
            this.minHeapify(i);
        }
    }
}

module.exports = BuildHeap;
