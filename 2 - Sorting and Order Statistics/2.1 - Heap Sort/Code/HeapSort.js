/**
 * HeapSort.js
 *
 */

const BuildHeap = require("./BuildHeap");

class HeapSort extends BuildHeap {
    constructor(heap) {
        super(heap);
        this.n = this.heapSize - 1;
    }

    heapSort() {
        this.buildMaxHeap();

        for (let i = this.n; i > 0; i--) {
            let temp = this.heap[0];
            this.heap[0] = this.heap[i];
            this.heap[i] = temp;
            this.heapSize -= 1;
            this.maxHeapify(0);
        }
    }
}

module.exports = HeapSort;
