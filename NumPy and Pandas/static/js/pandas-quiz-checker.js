function checkQuiz() {
  const questions = document.querySelectorAll('.test');
  let correct = 0;

  questions.forEach(q => {
    const correctAnswer = q.getAttribute('data-correct');
    const selected = q.querySelector('input[type="radio"]:checked');

    if (selected) {
      const isCorrect = selected.value === correctAnswer;
      q.style.backgroundColor = isCorrect ? "#d4edda" : "#f8d7da"; // green or red
      if (isCorrect) correct++;
    } else {
      q.style.backgroundColor = "#fff3cd"; // yellow if unanswered
    }
  });

  document.getElementById("result").innerHTML =
    `<h3>✅ You got ${correct} out of ${questions.length} correct!</h3>`;
}
