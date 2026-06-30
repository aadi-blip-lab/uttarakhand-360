/* ==========================================================
   UTTARAKHAND 360
   Version 1.0
========================================================== */

document.addEventListener("DOMContentLoaded", () => {

    startClock();

    setupTheme();

    setupSearch();

});


/* ==========================================================
   LIVE INDIA CLOCK
========================================================== */

function startClock() {

    const clock = document.getElementById("clock");

    if (!clock) return;

    function updateClock() {

        const now = new Date();

        clock.textContent = now.toLocaleTimeString("en-IN", {
            timeZone: "Asia/Kolkata",
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
            hour12: true
        });

    }

    updateClock();

    setInterval(updateClock, 1000);

}


/* ==========================================================
   DARK MODE
========================================================== */

function setupTheme() {

    const button = document.getElementById("theme-toggle");

    if (!button) return;

    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {

        document.body.classList.add("dark");

        button.textContent = "☀";

    }

    button.addEventListener("click", () => {

        document.body.classList.toggle("dark");

        const dark = document.body.classList.contains("dark");

        button.textContent = dark ? "☀" : "🌙";

        localStorage.setItem("theme", dark ? "dark" : "light");

    });

}


/* ==========================================================
   SEARCH
========================================================== */

function setupSearch() {

    const search = document.getElementById("search");

    if (!search) return;

    search.addEventListener("keyup", function () {

        const value = this.value.toLowerCase();

        const cards = document.querySelectorAll(".weather-card");

        cards.forEach(card => {

            const city = card.querySelector("h2");

            if (!city) return;

            if (city.textContent.toLowerCase().includes(value)) {

                card.style.display = "";

            } else {

                card.style.display = "none";

            }

        });

    });

}


/* ==========================================================
   SMOOTH PAGE LOAD
========================================================== */

window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});
