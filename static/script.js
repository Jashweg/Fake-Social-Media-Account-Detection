document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("prediction-form");
    const resultContainer = document.getElementById("result-container");
    const resultBox = document.getElementById("result-box");
    const resultText = document.getElementById("result-text");
    const submitBtn = document.getElementById("submit-btn");
    const btnText = submitBtn.querySelector("span");
    const loader = submitBtn.querySelector(".loader");
    const resetBtn = document.getElementById("reset-btn");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        // UI Loading state
        btnText.classList.add("hidden");
        loader.classList.remove("hidden");
        submitBtn.disabled = true;

        try {
            const formData = new FormData(form);
            
            const response = await fetch("/predict", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const data = await response.json();
            
            // Hide form, show result
            form.classList.add("hidden");
            resultContainer.classList.remove("hidden");
            
            resultText.textContent = data.prediction;
            document.getElementById("confidence-text").textContent = `Confidence: ${data.confidence}%`;
            
            // Styling based on prediction
            resultBox.className = "result-box"; // reset classes
            if (data.prediction.toLowerCase().includes("fake")) {
                resultBox.classList.add("fake");
            } else {
                resultBox.classList.add("original");
            }

        } catch (error) {
            alert("An error occurred while making the prediction. Please check the console for details.");
            console.error(error);
        } finally {
            // Restore UI state
            btnText.classList.remove("hidden");
            loader.classList.add("hidden");
            submitBtn.disabled = false;
        }
    });

    resetBtn.addEventListener("click", () => {
        form.reset();
        resultContainer.classList.add("hidden");
        form.classList.remove("hidden");
    });
});
