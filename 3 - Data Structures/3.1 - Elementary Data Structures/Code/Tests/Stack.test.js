/**
 * Stack.test.js
 *
 */

const Stack = require("../Stack");

let testStack = new Stack(4);

test("Stack underflow detected properly", () => {
    expect(() => {
        testStack.pop();
    }).toThrow(new EvalError("Stack underflow"));
});

test("Empty stack detected properly", () => {
    expect(testStack.stackEmpty()).toStrictEqual(true);
});

test("Stack responds properly to push operations", () => {
    testStack.push(55);
    testStack.push(23);
    testStack.push(11);

    expect(testStack.stack).toStrictEqual([55, 23, 11, NaN]);
    expect(testStack.top).toStrictEqual(3);
});

test("Stack overflow occurs when you push too many elements", () => {
    testStack.push(62);

    expect(() => {
        testStack.push(77);
    }).toThrow(new EvalError("Stack overflow"));
});

test("Operation pop works properly", () => {
    let popped = new Array();
    let tops = new Array();

    for (let i = 0; i < testStack.size; i++) {
        popped.push(testStack.pop());
        tops.push(testStack.top);
    }

    expect(popped).toStrictEqual([62, 11, 23, 55]);
    expect(tops).toStrictEqual([3, 2, 1, 0]);
});
