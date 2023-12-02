/**
 * TestHelpers.js
 *
 */

const isMaxHeap = (heap) => {
    for (let i = 0; i < heap.length; i++) {
        let leftChild = 2 * i + 1;
        let rightChild = 2 * i + 2;

        if (leftChild < heap.length && heap[i] < heap[leftChild]) {
            return false;
        }

        if (rightChild < heap.length && heap[i] < heap[rightChild]) {
            return false;
        }

        return true;
    }
};

const isMinHeap = (heap) => {
    for (let i = 0; i < heap.length; i++) {
        let leftChild = 2 * i + 1;
        let rightChild = 2 * i + 2;

        if (leftChild < heap.length && heap[i] > heap[leftChild]) {
            return false;
        }

        if (rightChild < heap.length && heap[i] > heap[rightChild]) {
            return false;
        }

        return true;
    }
};

module.exports = { isMinHeap, isMaxHeap };
