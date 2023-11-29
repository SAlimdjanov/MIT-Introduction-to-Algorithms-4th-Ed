/*
 * HiringProblem.mjs
 *
 */

export function hireAssistant(candidatesList, n) {
    let best = 0;
    let hiredCandidates = [];

    for (let i = 0; i < n; i++) {
        if (candidatesList[i] > best) {
            best = candidatesList[i];
            hiredCandidates.push(i);
        }
    }

    return hiredCandidates;
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

function permuteArray(array, n) {
    for (let i = 0; i < n; i++) {
        let temp = array[i];
        array[i] = array[getRandomInt(i, n)];
        array[getRandomInt(i, n)] = temp;
    }
}

export function randomizedHireAssistant(candidatesList, n) {
    permuteArray(candidatesList, n);
    let result = hireAssistant(candidatesList, n);
    return result;
}

export function onlineHiringProblem(k, n, scoresList) {
    let bestScore = Number.NEGATIVE_INFINITY;

    for (let i = 0; i < k; i++) {
        if (scoresList[i] > bestScore) {
            bestScore = scoresList[i];
        }
    }

    for (let j = k; j < n; j++) {
        if (scoresList[j] > bestScore) {
            return j;
        }
    }

    return n - 1;
}

const main = () => {
    let candidates = [3, 2, 6, 4, 5, 1];
    console.log(hireAssistant(candidates, candidates.length));
    console.log(randomizedHireAssistant(candidates, candidates.length));

    let k = 3;
    let scores = [4, 7, 2, 10, 2, 6];
    console.log(onlineHiringProblem(k, scores.length, scores));
};

// main();
