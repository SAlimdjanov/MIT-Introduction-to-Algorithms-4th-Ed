/**
 * HeapSort.mjs
 *
 */

import BuildHeap from "./BuildHeap.mjs";

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

const main = () => {
    let inputArray = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1];
    let sortHeap = new HeapSort(inputArray);
    sortHeap.heapSort();
    console.log(`Sorted Heap: ${sortHeap.heap}`);
};

// main();

export default HeapSort;
