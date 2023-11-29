/**
 * Heaps.mjs
 *
 */

class Heap {
    constructor(heap) {
        this.heap = heap;
    }

    parent(index) {
        return Math.floor((index - 1) / 2);
    }

    leftChild(index) {
        return 2 * index + 1;
    }

    rightChild(index) {
        return 2 * (index + 1);
    }
}

const main = () => {
    let maxHeap = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1];
    let myMaxHeap = new Heap(maxHeap);
    let childIndex = 1;
    let parentIndex = 1;

    let parentNode = maxHeap[myMaxHeap.parent(childIndex)];
    let leftChildNode = maxHeap[myMaxHeap.leftChild(parentIndex)];
    let rightChildNode = maxHeap[myMaxHeap.rightChild(parentIndex)];

    console.log(`The parent of node ${maxHeap[childIndex]} is ${parentNode}`);
    console.log(
        `The left child of node ${maxHeap[parentIndex]} is ${leftChildNode}`
    );
    console.log(
        `The right child of node ${maxHeap[parentIndex]} is ${rightChildNode}`
    );
};

// main();

export default Heap;
