/**
 * HiringProblem.test.js
 *
 */

const { hireAssistant, onlineHiringProblem } = require("../HiringProblem");
const { randomInt, permuteArray } = require("./TestHelpers");

test("Function hireAssistant hires the correct candidates", () => {
    const candidates = [3, 2, 6, 4, 5, 1];
    const expectedResult = [0, 2];

    let hireResult = hireAssistant(candidates, candidates.length);

    expect(hireResult).toStrictEqual(expectedResult);
});

test("Function onlineHiringProblem hires the correct candidates", () => {
    const k = 3;
    const scores = [4, 7, 2, 10, 2, 6];

    let selectedCandidate = onlineHiringProblem(k, scores.length, scores);
    let expectedResult = scores.indexOf(10);

    expect(selectedCandidate).toStrictEqual(expectedResult);
});
