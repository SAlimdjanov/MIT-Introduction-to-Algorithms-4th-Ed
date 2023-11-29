/*
 * BubbleSort.mjs
 *
 */

function bubbleSort(array) {
    let n = array.length;

    for (let i = 0; i < n; i++) {
        for (let j = n - 1; j > -1; j--) {
            if (array[j] < array[j - 1]) {
                let temp = array[j];
                array[j] = array[j - 1];
                array[j - 1] = temp;
            }
        }
    }
}

const main = () => {
    var array = [2, 4, 6, 7, 1, 2, 3, 5, 8, 10, 9];
    bubbleSort(array);

    console.log(array);
};

// main();

export default bubbleSort();
