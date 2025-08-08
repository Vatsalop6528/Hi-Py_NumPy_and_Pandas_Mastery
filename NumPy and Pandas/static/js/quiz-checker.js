function checkQuiz() {
  const questions = document.querySelectorAll('.question');
  let correct = 0;

  questions.forEach((q, i) => {
    const correctAnswer = q.getAttribute('data-correct');
    const selected = q.querySelector('input[type="radio"]:checked');

    if (selected) {
      const isCorrect = selected.value === correctAnswer;
      if (isCorrect) {
        q.style.backgroundColor = "#d4edda"; // green
        correct++;
      } else {
        q.style.backgroundColor = "#f8d7da"; // red
      }
    } else {
      q.style.backgroundColor = "#fff3cd"; // yellow - unanswered
    }
  });

  const scoreBox = document.getElementById("result");
  scoreBox.innerHTML = `<h3>✅ You got ${correct} out of ${questions.length} correct!</h3>`;
}

