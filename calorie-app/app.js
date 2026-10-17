const categories = ["Tout", "Fruits & légumes", "Féculents", "Protéines", "Produits laitiers", "Autres"];

const defaultFoods = [
  { id: "pomme", name: "Pomme", category: "Fruits & légumes", calories: 52, emoji: "🍎" },
  { id: "banane", name: "Banane", category: "Fruits & légumes", calories: 89, emoji: "🍌" },
  { id: "avocat", name: "Avocat", category: "Fruits & légumes", calories: 160, emoji: "🥑" },
  { id: "tomate", name: "Tomate", category: "Fruits & légumes", calories: 18, emoji: "🍅" },
  { id: "carotte", name: "Carotte", category: "Fruits & légumes", calories: 41, emoji: "🥕" },
  { id: "brocoli", name: "Brocoli", category: "Fruits & légumes", calories: 34, emoji: "🥦" },
  { id: "salade", name: "Salade verte", category: "Fruits & légumes", calories: 15, emoji: "🥬" },
  { id: "pdt", name: "Pomme de terre cuite", category: "Féculents", calories: 87, emoji: "🥔" },
  { id: "riz", name: "Riz blanc cuit", category: "Féculents", calories: 130, emoji: "🍚" },
  { id: "pates", name: "Pâtes cuites", category: "Féculents", calories: 157, emoji: "🍝" },
  { id: "pain", name: "Pain complet", category: "Féculents", calories: 247, emoji: "🍞" },
  { id: "quinoa", name: "Quinoa cuit", category: "Féculents", calories: 120, emoji: "🥣" },
  { id: "poulet", name: "Blanc de poulet cuit", category: "Protéines", calories: 165, emoji: "🍗" },
  { id: "saumon", name: "Saumon cuit", category: "Protéines", calories: 206, emoji: "🐟" },
  { id: "oeuf", name: "Œuf entier", category: "Protéines", calories: 143, emoji: "🥚" },
  { id: "tofu", name: "Tofu nature", category: "Protéines", calories: 144, emoji: "🧊" },
  { id: "lentilles", name: "Lentilles cuites", category: "Protéines", calories: 116, emoji: "🫘" },
  { id: "steak", name: "Bœuf haché cuit", category: "Protéines", calories: 250, emoji: "🥩" },
  { id: "yaourt", name: "Yaourt nature", category: "Produits laitiers", calories: 61, emoji: "🥛" },
  { id: "fromage", name: "Emmental", category: "Produits laitiers", calories: 380, emoji: "🧀" },
  { id: "fromage-blanc", name: "Fromage blanc 3 %", category: "Produits laitiers", calories: 75, emoji: "🥣" },
  { id: "huile", name: "Huile d’olive", category: "Autres", calories: 884, emoji: "🫒" },
  { id: "beurre", name: "Beurre", category: "Autres", calories: 717, emoji: "🧈" },
  { id: "amandes", name: "Amandes", category: "Autres", calories: 579, emoji: "🥜" },
  { id: "chocolat", name: "Chocolat noir", category: "Autres", calories: 546, emoji: "🍫" }
];

const keys = {
  foods: "atable-custom-foods",
  meal: "atable-current-meal",
  history: "atable-meal-history"
};

const elements = {
  categories: document.querySelector("#category-list"),
  search: document.querySelector("#food-search"),
  foodList: document.querySelector("#food-list"),
  mealName: document.querySelector("#meal-name"),
  mealItems: document.querySelector("#meal-items"),
  emptyState: document.querySelector("#empty-state"),
  total: document.querySelector("#total-calories"),
  totalCaption: document.querySelector("#total-caption"),
  saveButton: document.querySelector("#save-meal-button"),
  clearButton: document.querySelector("#clear-meal-button"),
  history: document.querySelector("#history-list"),
  historyEmpty: document.querySelector("#history-empty"),
  historyCount: document.querySelector("#history-count"),
  dialog: document.querySelector("#custom-food-dialog"),
  customForm: document.querySelector("#custom-food-form"),
  customName: document.querySelector("#custom-food-name"),
  customCalories: document.querySelector("#custom-food-calories"),
  formError: document.querySelector("#form-error"),
  toast: document.querySelector("#toast")
};

let activeCategory = "Tout";
let customFoods = readStorage(keys.foods, []);
let meal = readStorage(keys.meal, { name: "", items: [] });
let history = readStorage(keys.history, []);
let toastTimer;
let installPrompt;

function readStorage(key, fallback) {
  try {
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : fallback;
  } catch (error) {
    console.error(`Impossible de lire les données locales (${key}).`, error);
    return fallback;
  }
}

function saveStorage(key, value) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
    return true;
  } catch (error) {
    console.error(`Impossible d’enregistrer les données locales (${key}).`, error);
    showToast("Enregistrement impossible : vérifiez l’espace disponible sur l’appareil.");
    return false;
  }
}

function allFoods() {
  return [...defaultFoods, ...customFoods];
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, character => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  })[character]);
}

function renderCategories() {
  elements.categories.innerHTML = categories.map(category =>
    `<button type="button" class="category-chip${category === activeCategory ? " active" : ""}" aria-pressed="${category === activeCategory}" data-category="${escapeHtml(category)}">${escapeHtml(category)}</button>`
  ).join("");
}

function renderFoods() {
  const query = elements.search.value.trim().toLocaleLowerCase("fr");
  const matches = allFoods().filter(food =>
    (activeCategory === "Tout" || food.category === activeCategory) &&
    food.name.toLocaleLowerCase("fr").includes(query)
  );

  if (!matches.length) {
    elements.foodList.innerHTML = '<p class="no-results">Aucun aliment trouvé. Essayez un autre mot ou ajoutez votre aliment.</p>';
    return;
  }

  elements.foodList.innerHTML = matches.map(food => `
    <button type="button" class="food-row" data-food-id="${escapeHtml(food.id)}" aria-label="Ajouter ${escapeHtml(food.name)}, ${food.calories} kilocalories pour 100 grammes">
      <span class="food-emoji" aria-hidden="true">${escapeHtml(food.emoji || "🍽️")}</span>
      <span class="food-info"><span class="food-name">${escapeHtml(food.name)}</span><span class="food-category">${escapeHtml(food.category)}</span></span>
      <span class="food-kcal"><strong>${food.calories}</strong> kcal / 100 g</span>
      <span class="add-mark" aria-hidden="true">+</span>
    </button>`
  ).join("");
}

function renderMeal() {
  elements.mealName.value = meal.name || "";
  const totalCalories = meal.items.reduce((sum, item) => sum + item.calories * item.grams / 100, 0);
  const itemCount = meal.items.length;
  elements.total.textContent = Math.round(totalCalories).toLocaleString("fr-FR");
  elements.totalCaption.textContent = `${itemCount} aliment${itemCount > 1 ? "s" : ""}`;
  elements.emptyState.hidden = itemCount > 0;
  elements.mealItems.innerHTML = meal.items.map((item, index) => `
    <div class="meal-item">
      <span class="food-emoji" aria-hidden="true">${escapeHtml(item.emoji || "🍽️")}</span>
      <div class="meal-item-main">
        <span class="meal-item-name">${escapeHtml(item.name)}</span>
        <label class="meal-item-sub"><input class="quantity-input" type="number" min="0.1" max="10000" step="1" value="${item.grams}" data-quantity="${index}" aria-label="Quantité de ${escapeHtml(item.name)} en grammes"> g <span>· ${item.calories} kcal / 100 g</span></label>
      </div>
      <div class="item-kcal"><strong>${Math.round(item.calories * item.grams / 100).toLocaleString("fr-FR")}</strong> kcal</div>
      <button type="button" class="remove-item" data-remove="${index}" aria-label="Retirer ${escapeHtml(item.name)}">×</button>
    </div>`
  ).join("");
  elements.saveButton.disabled = itemCount === 0;
  elements.clearButton.disabled = itemCount === 0;
  saveStorage(keys.meal, meal);
}

function renderHistory() {
  const count = history.length;
  elements.historyCount.textContent = `${count} repas`;
  elements.historyEmpty.hidden = count > 0;
  elements.history.innerHTML = history.map((entry, index) => {
    const date = new Date(entry.date).toLocaleDateString("fr-FR", { day: "numeric", month: "short" });
    const itemsText = `${entry.items.length} aliment${entry.items.length > 1 ? "s" : ""} · ${date}`;
    return `<article class="history-card">
      <div><div class="history-card-title">${escapeHtml(entry.name || "Mon repas")}</div><div class="history-card-meta">${itemsText}</div></div>
      <div class="history-card-actions"><div class="history-card-calories">${entry.total.toLocaleString("fr-FR")} <span>kcal</span></div>
      <button type="button" class="history-open" data-open-history="${index}" aria-label="Ouvrir ${escapeHtml(entry.name || "ce repas")}">Ouvrir</button>
      <button type="button" class="history-delete" data-delete-history="${index}" aria-label="Supprimer ${escapeHtml(entry.name || "ce repas")}">×</button></div>
    </article>`;
  }).join("");
}

function showToast(message) {
  elements.toast.textContent = message;
  elements.toast.classList.add("visible");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => elements.toast.classList.remove("visible"), 2600);
}

function addFood(food) {
  const existing = meal.items.find(item => item.id === food.id);
  if (existing) {
    existing.grams += 100;
  } else {
    meal.items.push({ ...food, grams: 100 });
  }
  renderMeal();
}

function renderAll() {
  renderCategories();
  renderFoods();
  renderMeal();
  renderHistory();
}

elements.categories.addEventListener("click", event => {
  const button = event.target.closest("[data-category]");
  if (!button) return;
  activeCategory = button.dataset.category;
  renderCategories();
  renderFoods();
});

elements.search.addEventListener("input", renderFoods);

elements.foodList.addEventListener("click", event => {
  const row = event.target.closest("[data-food-id]");
  if (!row) return;
  const food = allFoods().find(item => item.id === row.dataset.foodId);
  if (food) addFood(food);
});

elements.mealItems.addEventListener("change", event => {
  const input = event.target.closest("[data-quantity]");
  if (!input) return;
  const grams = Number(input.value);
  if (!Number.isFinite(grams) || grams <= 0 || grams > 10000) return;
  meal.items[Number(input.dataset.quantity)].grams = grams;
  renderMeal();
});

elements.mealItems.addEventListener("click", event => {
  const button = event.target.closest("[data-remove]");
  if (!button) return;
  meal.items.splice(Number(button.dataset.remove), 1);
  renderMeal();
});

elements.mealName.addEventListener("input", () => {
  meal.name = elements.mealName.value;
  saveStorage(keys.meal, meal);
});

elements.clearButton.addEventListener("click", () => {
  meal = { name: "", items: [] };
  renderMeal();
  showToast("Votre assiette a été vidée.");
});

elements.saveButton.addEventListener("click", () => {
  if (!meal.items.length) return;
  const total = Math.round(meal.items.reduce((sum, item) => sum + item.calories * item.grams / 100, 0));
  history.unshift({
    id: crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random()}`,
    name: meal.name.trim() || "Mon repas",
    date: new Date().toISOString(),
    total,
    items: meal.items.map(item => ({ ...item }))
  });
  if (saveStorage(keys.history, history)) {
    renderHistory();
    showToast("Repas enregistré sur cet appareil.");
  }
});

elements.history.addEventListener("click", event => {
  const openButton = event.target.closest("[data-open-history]");
  const deleteButton = event.target.closest("[data-delete-history]");
  if (openButton) {
    const entry = history[Number(openButton.dataset.openHistory)];
    if (!entry) return;
    meal = { name: entry.name, items: entry.items.map(item => ({ ...item })) };
    renderMeal();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
  if (deleteButton) {
    history.splice(Number(deleteButton.dataset.deleteHistory), 1);
    if (saveStorage(keys.history, history)) renderHistory();
  }
});

document.querySelector("#custom-food-button").addEventListener("click", () => {
  elements.formError.textContent = "";
  elements.customForm.reset();
  elements.dialog.showModal();
  elements.customName.focus();
});

document.querySelector("#dialog-close").addEventListener("click", () => elements.dialog.close());
elements.dialog.addEventListener("click", event => {
  if (event.target === elements.dialog) elements.dialog.close();
});

elements.customForm.addEventListener("submit", event => {
  event.preventDefault();
  const name = elements.customName.value.trim();
  const calories = Number(elements.customCalories.value);
  if (!name || !Number.isFinite(calories) || calories < 0 || calories > 1000) {
    elements.formError.textContent = "Saisissez un nom et une valeur entre 0 et 1 000 kcal.";
    return;
  }
  const food = {
    id: `custom-${Date.now()}`,
    name,
    category: "Mes aliments",
    calories,
    emoji: "🍽️"
  };
  customFoods.push(food);
  if (!saveStorage(keys.foods, customFoods)) {
    customFoods.pop();
    return;
  }
  activeCategory = "Tout";
  elements.search.value = "";
  renderCategories();
  renderFoods();
  addFood(food);
  elements.dialog.close();
  showToast("Aliment ajouté à votre assiette et à vos aliments.");
});

document.addEventListener("keydown", event => {
  if (event.key === "/" && !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName) && !elements.dialog.open) {
    event.preventDefault();
    elements.search.focus();
  }
});

window.addEventListener("beforeinstallprompt", event => {
  event.preventDefault();
  installPrompt = event;
  const button = document.querySelector("#install-button");
  button.hidden = false;
  button.addEventListener("click", async () => {
    if (!installPrompt) return;
    installPrompt.prompt();
    await installPrompt.userChoice;
    installPrompt = null;
    button.hidden = true;
  }, { once: true });
});

document.querySelector("#meal-date").textContent = new Intl.DateTimeFormat("fr-FR", { weekday: "short", day: "numeric", month: "short" }).format(new Date());
renderAll();

if ("serviceWorker" in navigator && location.protocol !== "file:") {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("./service-worker.js").catch(error => {
      console.error("L’application hors ligne n’a pas pu être activée.", error);
    });
  });
}
