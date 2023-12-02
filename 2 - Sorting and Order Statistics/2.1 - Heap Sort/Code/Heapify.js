/**
 * Heapify.js
 *
 */

const Heap = require("./Heaps");

class Heapify extends Heap {
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

module.exports = Heapify;
