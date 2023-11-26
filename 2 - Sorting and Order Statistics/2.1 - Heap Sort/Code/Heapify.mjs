/**
 * Heapify.mjs
 *
 */

import Heap from "./Heaps.mjs";

export default class Heapify extends Heap {
    constructor(heap) {
        super(heap);
        this.heapSize = heap.length;
    }

    maxHeapify(index) {
        let left = this.leftChild(index);
        let right = this.rightChild(index);
        let largest = -1;

        if (left < this.heapSize && this.heap[left] > this.heap[index]) {
            largest = left;
        } else {
            largest = index;
        }

        if (right < this.heapSize && this.heap[right] > this.heap[largest]) {
            largest = right;
        }

        if (largest != index) {
            let temp = this.heap[index];
            this.heap[index] = this.heap[largest];
            this.heap[largest] = temp;
            this.maxHeapify(largest);
        }
    }

    minHeapify(index) {
        let left = this.leftChild(index);
        let right = this.rightChild(index);
        let smallest = index;

        if (left < this.heapSize && this.heap[left] < this.heap[index]) {
            smallest = left;
        } else {
            smallest = index;
        }

        if (right < this.heapSize && this.heap[right] < this.heap[smallest]) {
            smallest = right;
        }

        if (smallest != index) {
            let temp = this.heap[index];
            this.heap[index] = this.heap[smallest];
            this.heap[smallest] = temp;
            this.minHeapify(smallest);
        }
    }
}

const main = () => {
    const maxArray = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1];
    let heapifyMax = new Heapify(maxArray);
    heapifyMax.maxHeapify(1);
    console.log(heapifyMax.heap);

    const minArray = [1, 3, 14, 4, 7, 8, 9, 2, 10, 16];
    let heapifyMin = new Heapify(minArray);
    heapifyMin.minHeapify(2);
    console.log(heapifyMin.heap);
};

// main();
