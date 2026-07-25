// ================================
// THEME TOGGLE
// ================================

const themeBtn = document.getElementById("theme-toggle");

// Load saved theme
if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark");
    themeBtn.innerHTML = '<i class="fa-solid fa-sun"></i>';
} else {
    themeBtn.innerHTML = '<i class="fa-solid fa-moon"></i>';
}

// Toggle Theme
themeBtn.addEventListener("click", () => {

    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {

        localStorage.setItem("theme", "dark");

        themeBtn.innerHTML = '<i class="fa-solid fa-sun"></i>';

    } else {

        localStorage.setItem("theme", "light");

        themeBtn.innerHTML = '<i class="fa-solid fa-moon"></i>';

    }

});

// ================================
// PREDICT BUTTON LOADING
// ================================

const form = document.querySelector("form");
const predictBtn = document.querySelector(".predict-btn");

if (form) {

    form.addEventListener("submit", () => {

        predictBtn.disabled = true;

        predictBtn.innerHTML =
            '<i class="fa-solid fa-spinner fa-spin"></i> Predicting...';

    });

}

// ================================
// INPUT ANIMATION
// ================================

const inputs = document.querySelectorAll("input, select");

inputs.forEach((input) => {

    input.addEventListener("focus", () => {

        input.style.transform = "scale(1.02)";

    });

    input.addEventListener("blur", () => {

        input.style.transform = "scale(1)";

    });

});

// ================================
// PAGE FADE-IN
// ================================

window.addEventListener("load", () => {

    document.body.style.opacity = "0";

    document.body.style.transition = "opacity 0.6s ease";

    setTimeout(() => {

        document.body.style.opacity = "1";

    }, 100);

});