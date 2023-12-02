/**
 * PriorityQueue.test.js
 *
 */

const { constructQueue, MaxHeapPriorityQueue } = require("../PriorityQueue");

// Test Data

let heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1];

let tasks = [
    "Task 1",
    "Task 2",
    "Task 3",
    "Task 4",
    "Task 5",
    "Task 6",
    "Task 7",
    "Task 8",
    "Task 9",
    "Task 10",
];

let queue = constructQueue(heap, tasks);

let priorityQueue = new MaxHeapPriorityQueue(heap, tasks, queue);

// Tests

test("Method maximum returns max priority value", () => {
    expect(priorityQueue.maximum()).toStrictEqual(16);
});

test("Method extractMax returns max priority value and removes related data", () => {
    let expectedHeap = [...heap];
    let expectedTasks = [...tasks];
    let expectedQueue = queue;

    let maxPriority = priorityQueue.maximum();

    expectedHeap.shift();
    expectedTasks.shift();
    expectedQueue.delete(maxPriority);

    expect(priorityQueue.extractMax()).toStrictEqual(16);
    expect(expectedHeap).toStrictEqual(priorityQueue.heap);
    expect(expectedTasks).toStrictEqual(priorityQueue.tasks);
    expect(expectedQueue).toStrictEqual(priorityQueue.queue);
});

test("Method increaseKey increases the priority of an existing task", () => {
    let expectedHeap = [14, 11, 8, 10, 9, 3, 2, 4, 7];
    let expectedTasks = [
        "Task 2",
        "Task 10",
        "Task 4",
        "Task 3",
        "Task 6",
        "Task 7",
        "Task 8",
        "Task 9",
        "Task 5",
    ];
    let expectedQueue = constructQueue(expectedHeap, expectedTasks);

    priorityQueue.increaseKey(tasks[8], 11);

    expect(expectedHeap).toStrictEqual(priorityQueue.heap);
    expect(expectedTasks).toStrictEqual(priorityQueue.tasks);
    expect(expectedQueue).toStrictEqual(priorityQueue.queue);
});

test("Method insert adds a task with a priority value and correctly sorts relevant data", () => {
    let expectedHeap = [17, 14, 8, 10, 11, 3, 2, 4, 7, 9];
    let expectedTasks = [
        "Urgent Matter!",
        "Task 2",
        "Task 4",
        "Task 3",
        "Task 10",
        "Task 7",
        "Task 8",
        "Task 9",
        "Task 5",
        "Task 6",
    ];
    let expectedQueue = constructQueue(expectedHeap, expectedTasks);

    priorityQueue.insert("Urgent Matter!", 17);

    expect(expectedHeap).toStrictEqual(priorityQueue.heap);
    expect(expectedTasks).toStrictEqual(priorityQueue.tasks);
    expect(expectedQueue).toStrictEqual(priorityQueue.queue);
});
