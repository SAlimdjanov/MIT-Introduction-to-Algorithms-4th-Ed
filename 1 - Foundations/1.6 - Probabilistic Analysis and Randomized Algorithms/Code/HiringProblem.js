/*
 * HiringProblem.js
 *
 * JavaScript implementation of the Hiring Problem
 *
 */

function hireAssistant(candidatesList, n) {
    var best = 0;
    var hiredCandidates = [];

    for (var i = 0; i < n; i++) {
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
    for (var i = 0; i < n; i++) {
        let temp = array[i];
        array[i] = array[getRandomInt(i, n)];
        array[getRandomInt(i, n)] = temp;
    }
}

function randomizedHireAssistant(candidatesList, n) {
    permuteArray(candidatesList, n);
    let result = hireAssistant(candidatesList, n);
    return result;
}

function onlineHiringProblem(k, n, scoresList) {
    var bestScore = Number.NEGATIVE_INFINITY;

    for (var i = 0; i < k; i++) {
        if (scoresList[i] > bestScore) {
            bestScore = scoresList[i];
        }
    }

    for (var j = k; j < n; j++) {
        if (scoresList[j] > bestScore) {
            return j;
        }
    }

    return n - 1;
}

const candidates = [3, 2, 6, 4, 5, 1];
console.log(hireAssistant(candidates, candidates.length));
console.log(randomizedHireAssistant(candidates, candidates.length));

const k = 3;
const scores = [4, 7, 2, 10, 2, 6];
console.log(onlineHiringProblem(k, scores.length, scores));
