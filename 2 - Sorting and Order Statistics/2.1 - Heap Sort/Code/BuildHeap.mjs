/*
 * MaxHeapify.mjs
 *
 * JavaScript implementation of the MaxHeapify procedure
 *
 */

import Heapify from "./Heapify.mjs";

export default class ConstructHeap extends Heapify {
    constructor(heap) {
        super(heap);
    }

    buildMaxHeap() {
        for (var i = Math.floor(this.heapSize / 2); i > -1; i--) {
            this.maxHeapify(i);
        }
    }

    buildMinHeap() {
        for (var i = Math.floor(this.heapSize / 2); i > -1; i--) {
            this.minHeapify(i);
        }
    }
}

const main = () => {
    const array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7];
    console.log(`Input: ${array}`);

    let constructMaxHeap = new ConstructHeap(array);
    constructMaxHeap.buildMaxHeap();
    console.log(`Max Heap: ${constructMaxHeap.heap}`);

    let constructMinHeap = new ConstructHeap(array);
    constructMinHeap.buildMinHeap();
    console.log(`Min Heap: ${constructMinHeap.heap}`);
};

main();
