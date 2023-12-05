/**
 * Queue.js
 *
 */

class Queue {
    constructor(size) {
        this.size = size;
        this.queue = new Array(this.size).fill(NaN);
        this.tail = 0;
        this.head = 0;
    }

    dequeue() {
        if (this.head == this.tail) {
            throw new RangeError("Queue is empty");
        }

        let x = this.queue[this.head];
        this.queue[this.head] = NaN;

        if (this.tail == this.size) {
            this.head = 0;
        }

        this.queue.shift();
        this.queue.push(NaN);

        this.tail -= 1;

        return x;
    }

    enqueue(x) {
        if (this.tail == this.size) {
            throw new RangeError("Queue is full");
        }

        this.queue[this.tail] = x;
        this.tail += 1;
    }
}

module.exports = Queue;
