/**
 * BuildHeap.mjs
 *
 */

import Heapify from "./Heapify.mjs";

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

const main = () => {
    const array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7];
    console.log(`Input: ${array}`);

    let constructMaxHeap = new BuildHeap(array);
    constructMaxHeap.buildMaxHeap();
    console.log(`Max Heap: ${constructMaxHeap.heap}`);

    let constructMinHeap = new BuildHeap(array);
    constructMinHeap.buildMinHeap();
    console.log(`Min Heap: ${constructMinHeap.heap}`);
};

// main();

export default BuildHeap;
