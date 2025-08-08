function checkQuiz() {
    const questions = document.querySelectorAll(".question");
    let correct = 0;

    questions.forEach((question) => {
        const correctAnswer = question.getAttribute("data-answer");
        const selected = question.querySelector("input[type='radio']:checked");

        if (selected && selected.value === correctAnswer) {
            correct++;
            question.style.borderColor = "green";
        } else {
            question.style.borderColor = "red";
        }
    });

    const resultDiv = document.getElementById("result");
    resultDiv.textContent = `You got ${correct} out of ${questions.length} correct.`;
}
