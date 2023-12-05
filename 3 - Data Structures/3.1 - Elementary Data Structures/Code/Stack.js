/**
 * Stack.js
 *
 */

class Stack {
    constructor(size) {
        this.size = size;
        this.top = 0;
        this.stack = new Array(this.size).fill(NaN);
    }

    stackEmpty() {
        if (this.top == 0) {
            return true;
        }

        return false;
    }

    push(x) {
        if (this.top == this.size) {
            throw new RangeError("Stack overflow");
        }

        this.top += 1;
        this.stack[this.top - 1] = x;
    }

    pop() {
        if (this.stackEmpty()) {
            throw new RangeError("Stack underflow");
        }

        this.top -= 1;
        let value = this.stack[this.top];
        this.stack[this.top] = NaN;

        return value;
    }
}

module.exports = Stack;
