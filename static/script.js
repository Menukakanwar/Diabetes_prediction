document.getElementById('diabetesForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting

    // Get form values
    const age = document.getElementById('age').value;
    const gender = document.getElementById('gender').value;
    const bmi = document.getElementById('bmi').value;
    const glucose = document.getElementById('blood-glucose').value;
    const activity = document.getElementById('physical-activity').value;
    const familyHistory = document.getElementById('family-history').value;

    // Simple check to simulate risk prediction
    let risk = "Low";
    if (bmi > 25 || glucose > 100 || familyHistory === "Yes") {
        risk = "High";
    }

    // Show result
    const result = document.getElementById('result');
    result.textContent = `Your predicted diabetes risk is: ${risk}`;
});
