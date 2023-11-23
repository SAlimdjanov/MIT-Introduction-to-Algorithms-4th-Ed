/*
 * MaxHeapify.mjs
 *
 * JavaScript implementation of the MaxHeapify procedure
 *
 */

import Heap from "./Heaps.mjs";

class Heapify extends Heap {
    constructor(heap) {
        super(heap);
        this.heapSize = heap.length;
    }

    maxHeapify(index) {
        let left = this.leftChild(index);
        let right = this.rightChild(index);
        let largest = -1;

        if (left <= this.heapSize && this.heap[left] > this.heap[index]) {
            largest = left;
        } else {
            largest = index;
        }

        if (right <= this.heapSize && this.heap[right] > this.heap[largest]) {
            largest = right;
        }

        if (largest != index) {
            let temp = this.heap[index];
            this.heap[index] = this.heap[largest];
            this.heap[largest] = temp;
            this.maxHeapify(largest);
        }
    }
}

const main = () => {
    const array = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1];
    let heapify = new Heapify(array);
    heapify.maxHeapify(1);
    console.log(heapify.heap);
};

// main();
