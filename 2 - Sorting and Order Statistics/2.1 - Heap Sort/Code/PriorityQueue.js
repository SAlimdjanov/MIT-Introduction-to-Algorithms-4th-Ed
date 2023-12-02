/**
 * PriorityQueue.js
 *
 */

const Heapify = require("./Heapify");

class MaxHeapPriorityQueue extends Heapify {
    constructor(heap, tasks, queue) {
        super(heap);
        this.tasks = tasks;
        this.queue = queue;
    }

    maximum() {
        if (this.heapSize < 1) {
            throw new Error("Heap underflow");
        }

        return this.heap[0];
    }

    extractMax() {
        let maxElem = this.maximum();

        this.heap.shift();
        this.tasks.shift();
        this.queue.delete(maxElem);

        this.heapSize -= 1;
        this.maxHeapify(0);

        return maxElem;
    }

    increaseKey(selectedTask, k) {
        let oldKey = Number.NEGATIVE_INFINITY;

        for (let [key, val] of this.queue.entries()) {
            if (val === selectedTask) {
                oldKey = key;
            }
        }

        if (k < oldKey) {
            throw new Error("New key is smaller than the current key");
        }

        this.heap[this.heap.indexOf(oldKey)] = k;

        let i = this.heap.indexOf(k);

        while (i > 0 && this.heap[this.parent(i)] < this.heap[i]) {
            let temp1 = this.heap[i];
            this.heap[i] = this.heap[this.parent(i)];
            this.heap[this.parent(i)] = temp1;

            let temp2 = this.tasks[i];
            this.tasks[i] = this.tasks[this.parent(i)];
            this.tasks[this.parent(i)] = temp2;

            i = this.parent(i);
        }
        this.queue = constructQueue(this.heap, this.tasks);
    }

    insert(task, priority) {
        this.heapSize += 1;
        let k = priority;
        priority = Number.NEGATIVE_INFINITY;

        this.heap.push(priority);
        this.tasks.push(task);
        this.queue.set(priority, task);
        this.increaseKey(this.tasks[-1], k);
    }
}

const constructQueue = (keys, values) => {
    let queue = new Map();

    for (let i = 0; i < keys.length; i++) {
        queue.set(keys[i], values[i]);
    }

    return queue;
};

module.exports = { constructQueue, MaxHeapPriorityQueue };
