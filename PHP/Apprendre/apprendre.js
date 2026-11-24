const lessonCards = [...document.querySelectorAll("[data-lesson]")];
const completeButtons = [...document.querySelectorAll(".complete-button")];
const progressFill = document.querySelector("#progress-fill");
const progressLabel = document.querySelector("#progress-label");
const progressCaption = document.querySelector("#progress-caption");
const progressBar = document.querySelector('[role="progressbar"]');
const storageKey = "php-lab-completed-lessons";

function readCompletedLessons() {
    try {
        const saved = JSON.parse(localStorage.getItem(storageKey) ?? "[]");
        if (!Array.isArray(saved)) return new Set();
        return new Set(saved.filter((id) => lessonCards.some((card) => card.dataset.lesson === id)));
    } catch (error) {
        console.warn("La progression locale n'a pas pu être lue.", error);
        return new Set();
    }
}

let completedLessons = readCompletedLessons();

function updateProgress() {
    const count = completedLessons.size;
    const percent = Math.round((count / lessonCards.length) * 100);

    progressFill.style.width = `${percent}%`;
    progressLabel.textContent = `${count} / ${lessonCards.length}`;
    progressCaption.textContent = count === lessonCards.length
        ? "Bravo, tu as terminé le parcours !"
        : count === 0
            ? "À toi de jouer, le premier pas compte."
            : "Continue comme ça, tu progresses.";
    progressBar.setAttribute("aria-valuenow", String(count));

    lessonCards.forEach((card) => {
        const isComplete = completedLessons.has(card.dataset.lesson);
        const button = card.querySelector(".complete-button");
        card.classList.toggle("is-complete", isComplete);
        button.setAttribute("aria-pressed", String(isComplete));
        button.lastChild.textContent = isComplete ? " Terminé" : " Marquer comme terminé";
    });
}

completeButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const lessonId = button.closest("[data-lesson]").dataset.lesson;
        if (completedLessons.has(lessonId)) completedLessons.delete(lessonId);
        else completedLessons.add(lessonId);

        try {
            localStorage.setItem(storageKey, JSON.stringify([...completedLessons]));
        } catch (error) {
            console.warn("La progression ne peut pas être enregistrée sur cet appareil.", error);
        }
        updateProgress();
    });
});

document.querySelectorAll("[data-copy]").forEach((button) => {
    button.addEventListener("click", async () => {
        const code = document.getElementById(button.dataset.copy)?.textContent;
        if (!code) return;

        try {
            await navigator.clipboard.writeText(code);
            button.textContent = "Copié !";
            window.setTimeout(() => { button.textContent = "Copier le code"; }, 1600);
        } catch (error) {
            console.error("La copie dans le presse-papiers a échoué.", error);
            button.textContent = "Copie indisponible";
            window.setTimeout(() => { button.textContent = "Copier le code"; }, 1800);
        }
    });
});

const quizFeedback = document.querySelector("#quiz-feedback");
document.querySelectorAll(".quiz-option").forEach((option) => {
    option.addEventListener("click", () => {
        document.querySelectorAll(".quiz-option").forEach((item) => {
            item.classList.remove("is-correct", "is-wrong");
        });

        if (option.dataset.answer === "correct") {
            option.classList.add("is-correct");
            quizFeedback.textContent = "Exact ! Une requête préparée protège la structure de ta requête SQL.";
        } else {
            option.classList.add("is-wrong");
            quizFeedback.textContent = "Pas tout à fait. Cherche une méthode qui sépare la requête SQL de ses valeurs.";
        }
    });
});

updateProgress();
