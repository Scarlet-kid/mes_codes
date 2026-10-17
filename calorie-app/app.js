const categories = ["Tout", "Fruits & légumes", "Féculents", "Protéines", "Produits laitiers", "Autres", "Mes aliments"];

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
  history: "atable-meal-history",
  profile: "atable-profile",
  completedDays: "atable-completed-days",
  weighIns: "atable-weigh-ins",
  steps: "atable-daily-steps",
  stepsGoal: "atable-steps-goal",
  workouts: "atable-daily-workouts"
};

const today = localDateKey(new Date());
const elements = {
  categories: document.querySelector("#category-list"),
  search: document.querySelector("#food-search"),
  foodList: document.querySelector("#food-list"),
  mealName: document.querySelector("#meal-name"),
  mealDay: document.querySelector("#meal-day"),
  mealDate: document.querySelector("#meal-date"),
  mealItems: document.querySelector("#meal-items"),
  emptyState: document.querySelector("#empty-state"),
  total: document.querySelector("#total-calories"),
  totalCaption: document.querySelector("#total-caption"),
  loggedDayTotal: document.querySelector("#logged-day-total"),
  saveButton: document.querySelector("#save-meal-button"),
  clearButton: document.querySelector("#clear-meal-button"),
  completeDayButton: document.querySelector("#complete-day-button"),
  history: document.querySelector("#history-list"),
  historyEmpty: document.querySelector("#history-empty"),
  historyCount: document.querySelector("#history-count"),
  profileBanner: document.querySelector("#profile-banner"),
  profileStatus: document.querySelector("#profile-status"),
  profileDetail: document.querySelector("#profile-detail"),
  profileDialog: document.querySelector("#profile-dialog"),
  profileForm: document.querySelector("#profile-form"),
  profileError: document.querySelector("#profile-error"),
  reportMonth: document.querySelector("#report-month"),
  stepsMonthTotal: document.querySelector("#steps-month-total"),
  stepsDailyAverage: document.querySelector("#steps-daily-average"),
  stepsGoalDays: document.querySelector("#steps-goal-days"),
  stepsChart: document.querySelector("#steps-chart"),
  stepsForm: document.querySelector("#steps-form"),
  stepsDate: document.querySelector("#steps-date"),
  stepsCount: document.querySelector("#steps-count"),
  stepsGoal: document.querySelector("#steps-goal"),
  reportPlaceholder: document.querySelector("#report-placeholder"),
  monthlyReport: document.querySelector("#monthly-report"),
  averageIntake: document.querySelector("#average-intake"),
  trackedDays: document.querySelector("#tracked-days"),
  dailyTarget: document.querySelector("#daily-target"),
  monthlyChange: document.querySelector("#monthly-change"),
  monthlyChangeNote: document.querySelector("#monthly-change-note"),
  calorieChart: document.querySelector("#calorie-chart"),
  weightChart: document.querySelector("#weight-chart"),
  weighInForm: document.querySelector("#weigh-in-form"),
  weighInDate: document.querySelector("#weigh-in-date"),
  weighInWeight: document.querySelector("#weigh-in-weight"),
  workoutForm: document.querySelector("#workout-form"),
  workoutDate: document.querySelector("#workout-date"),
  workoutFields: document.querySelector("#workout-fields"),
  workoutType: document.querySelector("#workout-type"),
  workoutDuration: document.querySelector("#workout-duration"),
  workoutIntensity: document.querySelector("#workout-intensity"),
  workoutCalories: document.querySelector("#workout-calories"),
  workoutEstimate: document.querySelector("#workout-estimate"),
  dialog: document.querySelector("#custom-food-dialog"),
  customForm: document.querySelector("#custom-food-form"),
  customName: document.querySelector("#custom-food-name"),
  customCalories: document.querySelector("#custom-food-calories"),
  formError: document.querySelector("#form-error"),
  toast: document.querySelector("#toast")
};

let activeCategory = "Tout";
let customFoods = readStorage(keys.foods, []);
let meal = readStorage(keys.meal, { name: "", date: today, items: [] });
let history = readStorage(keys.history, []);
let profile = readStorage(keys.profile, null);
let completedDays = readStorage(keys.completedDays, []);
let weighIns = readStorage(keys.weighIns, {});
let steps = readStorage(keys.steps, {});
let stepsGoal = readStorage(keys.stepsGoal, 8000);
let workouts = readStorage(keys.workouts, {});
let toastTimer;
let installPrompt;

const tabList = document.querySelector('[role="tablist"]');
const tabButtons = [...tabList.querySelectorAll('[role="tab"]')];

function selectTab(button, moveFocus = false) {
  tabButtons.forEach(tab => {
    const isSelected = tab === button;
    tab.setAttribute("aria-selected", String(isSelected));
    tab.tabIndex = isSelected ? 0 : -1;
    document.getElementById(tab.getAttribute("aria-controls")).hidden = !isSelected;
  });
  if (moveFocus) button.focus();
  if (button.dataset.tab === "tab-report") renderReport();
  if (button.dataset.tab === "tab-activity") renderStepsReport();
}

tabList.addEventListener("click", event => {
  const button = event.target.closest('[role="tab"]');
  if (button) selectTab(button);
});

tabList.addEventListener("keydown", event => {
  const currentIndex = tabButtons.indexOf(document.activeElement);
  if (currentIndex < 0) return;

  let nextIndex;
  if (event.key === "ArrowRight") nextIndex = (currentIndex + 1) % tabButtons.length;
  if (event.key === "ArrowLeft") nextIndex = (currentIndex - 1 + tabButtons.length) % tabButtons.length;
  if (event.key === "Home") nextIndex = 0;
  if (event.key === "End") nextIndex = tabButtons.length - 1;
  if (nextIndex === undefined) return;

  event.preventDefault();
  selectTab(tabButtons[nextIndex], true);
});

if (!Array.isArray(customFoods)) customFoods = [];
if (!Array.isArray(history)) history = [];
if (!Array.isArray(completedDays)) completedDays = [];
if (!weighIns || typeof weighIns !== "object" || Array.isArray(weighIns)) weighIns = {};
if (!steps || typeof steps !== "object" || Array.isArray(steps)) steps = {};
steps = Object.fromEntries(Object.entries(steps).filter(([day, count]) =>
  /^\d{4}-\d{2}-\d{2}$/.test(day) && Number.isInteger(count) && count >= 0 && count <= 200000
));
if (!Number.isInteger(stepsGoal) || stepsGoal < 1000 || stepsGoal > 100000) stepsGoal = 8000;
if (!workouts || typeof workouts !== "object" || Array.isArray(workouts)) workouts = {};
workouts = Object.fromEntries(Object.entries(workouts).filter(([day, workout]) =>
  /^\d{4}-\d{2}-\d{2}$/.test(day) && workout && ["push", "pull", "abdo-jambe"].includes(workout.type) &&
  [3.5, 6].includes(workout.met) && Number.isInteger(workout.duration) && workout.duration >= 10 && workout.duration <= 240
));
if (!meal || !Array.isArray(meal.items)) meal = { name: "", date: today, items: [] };
if (!meal.date) meal.date = today;
if (!meal.id) meal.id = null;

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

function localDateKey(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

function dateFromKey(key) {
  return new Date(`${key}T12:00:00`);
}

function entryDay(entry) {
  if (entry.day && /^\d{4}-\d{2}-\d{2}$/.test(entry.day)) return entry.day;
  const date = new Date(entry.date);
  return Number.isNaN(date.getTime()) ? today : localDateKey(date);
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, character => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  })[character]);
}

function allFoods() {
  return [...defaultFoods, ...customFoods];
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

function caloriesForItems(items) {
  return items.reduce((sum, item) => sum + item.calories * item.grams / 100, 0);
}

function caloriesByDay() {
  const totals = new Map();
  for (const entry of history) {
    const day = entryDay(entry);
    const calories = Number.isFinite(entry.total) ? entry.total : caloriesForItems(entry.items || []);
    totals.set(day, (totals.get(day) || 0) + calories);
  }
  return totals;
}

function caloriesForDay(day) {
  return caloriesByDay().get(day) || 0;
}

function weightForDay(day) {
  const previousWeighIns = Object.entries(weighIns)
    .filter(([weighInDay, weight]) => weighInDay <= day && Number.isFinite(weight))
    .sort(([dayA], [dayB]) => dayB.localeCompare(dayA));
  return previousWeighIns.length ? previousWeighIns[0][1] : profile.weight;
}

function workoutCalories(workout, day) {
  if (!profile || !workout) return 0;
  return Math.round((workout.met - 1) * weightForDay(day) * workout.duration / 60);
}

function workoutForDay(day) {
  return workouts[day] || null;
}

function targetForDay(day) {
  return profile ? profile.target + workoutCalories(workoutForDay(day), day) : 0;
}

function expenditureForDay(day) {
  return profile ? profile.expenditure + workoutCalories(workoutForDay(day), day) : 0;
}

function renderWorkoutPreview() {
  const day = elements.workoutDate.value;
  const isTrainingDay = elements.workoutForm.querySelector('[name="workout-status"]:checked').value === "yes";
  elements.workoutFields.hidden = !isTrainingDay;

  const savedWorkout = workoutForDay(day);
  const workout = isTrainingDay ? {
    type: elements.workoutType.value,
    duration: Number(elements.workoutDuration.value),
    met: Number(elements.workoutIntensity.value)
  } : null;
  const activeCalories = workout && Number.isFinite(workout.duration) && workout.duration > 0
    ? workoutCalories(workout, day)
    : 0;

  elements.workoutCalories.textContent = `+${activeCalories.toLocaleString("fr-FR")} kcal`;
  if (!profile) {
    elements.workoutEstimate.textContent = isTrainingDay
      ? "Séance sélectionnée. Complétez votre profil pour estimer les calories et ajuster l’objectif."
      : "Aucune séance enregistrée pour cette date. Complétez votre profil pour afficher votre repère calorique.";
  } else if (isTrainingDay) {
    const target = profile.target + activeCalories;
    elements.workoutEstimate.textContent = `Environ ${activeCalories.toLocaleString("fr-FR")} kcal actives pour cette séance. Repère calorique du jour : ${target.toLocaleString("fr-FR")} kcal.`;
  } else {
    elements.workoutEstimate.textContent = `Aucune séance enregistrée pour cette date. Repère calorique : ${profile.target.toLocaleString("fr-FR")} kcal.`;
  }

  elements.workoutForm.querySelector(".workout-save").textContent =
    !isTrainingDay && !savedWorkout ? "Enregistrer le statut" : "Enregistrer le statut du jour";
}

function loadWorkoutForDate(day) {
  const workout = workoutForDay(day);
  elements.workoutForm.querySelector(`[name="workout-status"][value="${workout ? "yes" : "no"}"]`).checked = true;
  elements.workoutType.value = workout?.type || "push";
  elements.workoutDuration.value = String(workout?.duration || 60);
  elements.workoutIntensity.value = String(workout?.met || 3.5);
  renderWorkoutPreview();
}

function renderMeal() {
  elements.mealName.value = meal.name || "";
  elements.mealDay.value = meal.date;
  elements.mealDate.textContent = dateFromKey(meal.date).toLocaleDateString("fr-FR", { weekday: "short", day: "numeric", month: "short" });

  const itemCount = meal.items.length;
  const draftCalories = caloriesForItems(meal.items);
  const editedEntry = meal.id ? history.find(entry => entry.id === meal.id) : null;
  const savedDayCalories = caloriesForDay(meal.date) - (editedEntry
    ? (Number.isFinite(editedEntry.total) ? editedEntry.total : caloriesForItems(editedEntry.items || []))
    : 0);
  elements.loggedDayTotal.textContent = `${Math.round(Math.max(0, savedDayCalories + draftCalories)).toLocaleString("fr-FR")} kcal`;
  elements.total.textContent = Math.round(draftCalories).toLocaleString("fr-FR");
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
  elements.saveButton.innerHTML = meal.id
    ? "Enregistrer les modifications"
    : '<span aria-hidden="true">↗</span> Enregistrer ce repas';
  elements.clearButton.disabled = itemCount === 0;
  elements.completeDayButton.disabled = !profile || caloriesForDay(meal.date) <= 0;
  const isDayComplete = completedDays.includes(meal.date);
  elements.completeDayButton.textContent = isDayComplete ? "Journée validée" : "Valider la journée";
  elements.completeDayButton.setAttribute("aria-pressed", String(isDayComplete));
  saveStorage(keys.meal, meal);
}

function renderHistory() {
  elements.historyCount.textContent = `${history.length} repas`;
  elements.historyEmpty.hidden = history.length > 0;
  elements.history.innerHTML = history.map((entry, index) => {
    const date = dateFromKey(entryDay(entry)).toLocaleDateString("fr-FR", { day: "numeric", month: "short" });
    const itemsText = `${(entry.items || []).length} aliment${(entry.items || []).length > 1 ? "s" : ""} · ${date}`;
    const total = Number.isFinite(entry.total) ? entry.total : caloriesForItems(entry.items || []);
    return `<article class="history-card">
      <div><div class="history-card-title">${escapeHtml(entry.name || "Mon repas")}</div><div class="history-card-meta">${itemsText}</div></div>
      <div class="history-card-actions"><div class="history-card-calories">${Math.round(total).toLocaleString("fr-FR")} <span>kcal</span></div>
      <button type="button" class="history-open" data-open-history="${index}" aria-label="Modifier ${escapeHtml(entry.name || "ce repas")}">Modifier</button>
      <button type="button" class="history-delete" data-delete-history="${index}" aria-label="Supprimer ${escapeHtml(entry.name || "ce repas")}">×</button></div>
    </article>`;
  }).join("");
}

function calculateProfile(data) {
  const sexAdjustment = data.sex === "female" ? -161 : data.sex === "male" ? 5 : -78;
  const restingCalories = 10 * data.weight + 6.25 * data.height - 5 * data.age + sexAdjustment;
  const expenditure = Math.round(restingCalories * Number(data.activity));
  const target = expenditure >= 1750 ? expenditure - 250 : expenditure;
  return { ...data, activity: Number(data.activity), expenditure, target };
}

function renderProfile() {
  if (!profile) {
    elements.profileStatus.textContent = "Configurez votre profil pour commencer";
    elements.profileDetail.textContent = "Une estimation personnalisée de vos besoins sera calculée à partir de vos informations.";
    elements.reportPlaceholder.hidden = false;
    elements.monthlyReport.hidden = true;
    renderWorkoutPreview();
    return;
  }

  const targetDescription = profile.target < profile.expenditure
    ? `Objectif indicatif hors séance : environ ${profile.target.toLocaleString("fr-FR")} kcal/j (écart modéré estimé).`
    : "Aucun déficit automatique proposé ; le repère est votre dépense estimée, hors séance.";
  elements.profileStatus.textContent = `Dépense quotidienne estimée : environ ${profile.expenditure.toLocaleString("fr-FR")} kcal`;
  elements.profileDetail.textContent = `${targetDescription} Choisissez votre activité habituelle hors séances de musculation : celles-ci sont ajoutées séparément.`;
  elements.reportPlaceholder.hidden = true;
  elements.monthlyReport.hidden = false;
  renderWorkoutPreview();
}

function monthDays(month) {
  const [year, monthNumber] = month.split("-").map(Number);
  return new Date(year, monthNumber, 0).getDate();
}

function renderCalorieChart(month, dailyTotals) {
  const [year, monthNumber] = month.split("-").map(Number);
  const count = monthDays(month);
  const width = 600;
  const height = 220;
  const left = 38;
  const right = 8;
  const top = 14;
  const bottom = 28;
  const plotWidth = width - left - right;
  const plotHeight = height - top - bottom;
  const dayTargets = Array.from({ length: count }, (_, index) => {
    const day = `${year}-${String(monthNumber).padStart(2, "0")}-${String(index + 1).padStart(2, "0")}`;
    return targetForDay(day);
  });
  const maximum = Math.max(500, ...dayTargets.map(target => target * 1.2), ...Array.from(dailyTotals.values()).filter(Number.isFinite)) * 1.08;
  const y = value => top + plotHeight - value / maximum * plotHeight;
  const gap = plotWidth / count;
  const barWidth = Math.max(3, gap * 0.62);
  let markup = '<text class="chart-axis-label" x="8" y="12">kcal</text>';

  for (let tick = 0; tick <= 4; tick++) {
    const value = Math.round(maximum * tick / 4);
    const tickY = y(value);
    markup += `<line class="chart-grid-line" x1="${left}" y1="${tickY}" x2="${width - right}" y2="${tickY}"></line><text class="chart-axis-label" x="${left - 5}" y="${tickY + 3}" text-anchor="end">${value}</text>`;
  }

  const targetPoints = dayTargets.map((target, index) =>
    `${left + gap * (index + 0.5)},${y(target)}`
  ).join(" ");
  markup += `<polyline class="chart-target-line" points="${targetPoints}"><title>Objectif journalier, séance de musculation incluse les jours concernés</title></polyline>`;

  for (let day = 1; day <= count; day++) {
    const key = `${year}-${String(monthNumber).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
    const total = dailyTotals.get(key) || 0;
    if (total > 0) {
      const barHeight = Math.max(1, (total / maximum) * plotHeight);
      const x = left + gap * (day - 0.5) - barWidth / 2;
      const className = completedDays.includes(key) ? "chart-bar" : "chart-bar incomplete";
      markup += `<rect class="${className}" x="${x}" y="${top + plotHeight - barHeight}" width="${barWidth}" height="${barHeight}" rx="2"><title>${day} : ${Math.round(total)} kcal${completedDays.includes(key) ? " (journée complète)" : " (journée non confirmée complète)"}</title></rect>`;
    }
    const workout = workoutForDay(key);
    if (workout) {
      const target = targetForDay(key);
      markup += `<circle class="chart-target-point" cx="${left + gap * (day - 0.5)}" cy="${y(target)}" r="2.5"><title>${day} : objectif ajusté à ${target.toLocaleString("fr-FR")} kcal après ${workout.type} (${workoutCalories(workout, key)} kcal estimées)</title></circle>`;
    }
    if (day === 1 || day % 5 === 0 || day === count) {
      markup += `<text class="chart-axis-label" x="${left + gap * (day - 0.5)}" y="${height - 8}" text-anchor="middle">${day}</text>`;
    }
  }
  elements.calorieChart.setAttribute("viewBox", `0 0 ${width} ${height}`);
  elements.calorieChart.innerHTML = markup;
}

function projectedWeightAt(day, dailyTotals) {
  if (day < profile.startDate) return null;
  let cumulativeCalories = 0;
  for (const completeDay of completedDays) {
    if (completeDay >= profile.startDate && completeDay <= day) {
      cumulativeCalories += expenditureForDay(completeDay) - (dailyTotals.get(completeDay) || 0);
    }
  }
  return profile.startWeight - cumulativeCalories / 7700;
}

function renderWeightChart(month, dailyTotals) {
  const [year, monthNumber] = month.split("-").map(Number);
  const count = monthDays(month);
  const firstDay = `${year}-${String(monthNumber).padStart(2, "0")}-01`;
  const lastDay = `${year}-${String(monthNumber).padStart(2, "0")}-${String(count).padStart(2, "0")}`;
  const actuals = Object.entries(weighIns)
    .filter(([day, weight]) => day >= firstDay && day <= lastDay && Number.isFinite(weight))
    .sort(([dayA], [dayB]) => dayA.localeCompare(dayB));
  const completeInMonth = completedDays.filter(day => day >= firstDay && day <= lastDay && day >= profile.startDate).sort();
  const projected = completeInMonth.map(day => [day, projectedWeightAt(day, dailyTotals)]);
  if (profile.startDate >= firstDay && profile.startDate <= lastDay) {
    projected.unshift([profile.startDate, profile.startWeight]);
  }

  const values = [
    ...actuals.map(([, weight]) => weight),
    ...projected.map(([, weight]) => weight)
  ];
  const width = 600;
  const height = 220;
  const left = 38;
  const right = 8;
  const top = 14;
  const bottom = 28;
  const plotWidth = width - left - right;
  const plotHeight = height - top - bottom;

  if (!values.length) {
    elements.weightChart.setAttribute("viewBox", `0 0 ${width} ${height}`);
    elements.weightChart.innerHTML = `<text class="chart-axis-label" x="${width / 2}" y="${height / 2}" text-anchor="middle">Pas encore de pesée ou de journée complète ce mois</text>`;
    return;
  }

  const minWeight = Math.min(...values);
  const maxWeight = Math.max(...values);
  const padding = Math.max(0.5, (maxWeight - minWeight) * 0.2);
  const low = minWeight - padding;
  const high = maxWeight + padding;
  const x = day => left + ((Number(day.slice(-2)) - 1) / Math.max(1, count - 1)) * plotWidth;
  const y = weight => top + plotHeight - (weight - low) / (high - low) * plotHeight;
  let markup = '<text class="chart-axis-label" x="8" y="12">kg</text>';

  for (let tick = 0; tick <= 4; tick++) {
    const value = low + (high - low) * tick / 4;
    const tickY = y(value);
    markup += `<line class="chart-grid-line" x1="${left}" y1="${tickY}" x2="${width - right}" y2="${tickY}"></line><text class="chart-axis-label" x="${left - 5}" y="${tickY + 3}" text-anchor="end">${value.toFixed(1)}</text>`;
  }

  for (let day = 1; day <= count; day++) {
    if (day === 1 || day % 5 === 0 || day === count) {
      markup += `<text class="chart-axis-label" x="${x(`${year}-${String(monthNumber).padStart(2, "0")}-${String(day).padStart(2, "0")}`)}" y="${height - 8}" text-anchor="middle">${day}</text>`;
    }
  }

  if (projected.length) {
    const points = projected.map(([day, weight]) => `${x(day)},${y(weight)}`).join(" ");
    markup += `<polyline class="chart-projected-line" points="${points}"><title>Tendance théorique, calculée uniquement à partir des journées complètes</title></polyline>`;
    markup += projected.map(([day, weight]) => `<circle class="chart-projected-point" cx="${x(day)}" cy="${y(weight)}" r="3"><title>${dateFromKey(day).toLocaleDateString("fr-FR")} : tendance ${weight.toFixed(1)} kg</title></circle>`).join("");
  }
  markup += actuals.map(([day, weight]) => `<circle class="chart-weigh-in" cx="${x(day)}" cy="${y(weight)}" r="5"><title>${dateFromKey(day).toLocaleDateString("fr-FR")} : pesée ${weight.toFixed(1)} kg</title></circle>`).join("");
  elements.weightChart.setAttribute("viewBox", `0 0 ${width} ${height}`);
  elements.weightChart.innerHTML = markup;
}

function renderStepsReport() {
  const month = elements.reportMonth.value || today.slice(0, 7);
  const [year, monthNumber] = month.split("-").map(Number);
  const count = monthDays(month);
  const width = 600;
  const height = 220;
  const left = 48;
  const right = 8;
  const top = 14;
  const bottom = 28;
  const plotWidth = width - left - right;
  const plotHeight = height - top - bottom;
  const gap = plotWidth / count;
  const barWidth = Math.max(3, gap * 0.62);
  const dailySteps = Object.entries(steps).filter(([day, value]) =>
    day.startsWith(`${month}-`) && Number.isInteger(value) && value >= 0
  );
  const total = dailySteps.reduce((sum, [, value]) => sum + value, 0);
  const daysMet = dailySteps.filter(([, value]) => value >= stepsGoal).length;
  const average = dailySteps.length ? Math.round(total / dailySteps.length) : null;
  const maximum = Math.max(1000, stepsGoal * 1.15, ...dailySteps.map(([, value]) => value)) * 1.08;
  const y = value => top + plotHeight - value / maximum * plotHeight;
  let markup = '<text class="chart-axis-label" x="8" y="12">pas</text>';

  elements.stepsMonthTotal.textContent = total.toLocaleString("fr-FR");
  elements.stepsDailyAverage.textContent = average === null ? "—" : `${average.toLocaleString("fr-FR")} pas`;
  elements.stepsGoalDays.textContent = `${daysMet} / ${dailySteps.length}`;
  elements.stepsGoal.value = String(stepsGoal);

  for (let tick = 0; tick <= 4; tick++) {
    const value = Math.round(maximum * tick / 4 / 1000) * 1000;
    const tickY = y(value);
    markup += `<line class="chart-grid-line" x1="${left}" y1="${tickY}" x2="${width - right}" y2="${tickY}"></line><text class="chart-axis-label" x="${left - 5}" y="${tickY + 3}" text-anchor="end">${(value / 1000).toLocaleString("fr-FR")}k</text>`;
  }

  const targetY = y(stepsGoal);
  markup += `<line class="chart-target-line" x1="${left}" y1="${targetY}" x2="${width - right}" y2="${targetY}"><title>Objectif quotidien : ${stepsGoal.toLocaleString("fr-FR")} pas</title></line>`;

  for (let day = 1; day <= count; day++) {
    const date = `${year}-${String(monthNumber).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
    if (Object.prototype.hasOwnProperty.call(steps, date)) {
      const value = steps[date];
      if (value > 0) {
        const barHeight = Math.max(1, (value / maximum) * plotHeight);
        const x = left + gap * (day - 0.5) - barWidth / 2;
        markup += `<rect class="chart-bar steps-bar" x="${x}" y="${top + plotHeight - barHeight}" width="${barWidth}" height="${barHeight}" rx="2"><title>${day} : ${value.toLocaleString("fr-FR")} pas</title></rect>`;
      }
    }
    if (day === 1 || day % 5 === 0 || day === count) {
      markup += `<text class="chart-axis-label" x="${left + gap * (day - 0.5)}" y="${height - 8}" text-anchor="middle">${day}</text>`;
    }
  }

  elements.stepsChart.setAttribute("viewBox", `0 0 ${width} ${height}`);
  elements.stepsChart.innerHTML = markup;
}

function renderReport() {
  renderProfile();
  renderStepsReport();
  if (!profile) return;

  const month = elements.reportMonth.value || today.slice(0, 7);
  const [year, monthNumber] = month.split("-").map(Number);
  const firstDay = `${year}-${String(monthNumber).padStart(2, "0")}-01`;
  const lastDay = `${year}-${String(monthNumber).padStart(2, "0")}-${String(monthDays(month)).padStart(2, "0")}`;
  const dailyTotals = caloriesByDay();
  const totalsForMonth = [...dailyTotals.entries()].filter(([day]) => day >= firstDay && day <= lastDay && day >= profile.startDate);
  const completeForMonth = totalsForMonth.filter(([day]) => completedDays.includes(day) && day >= profile.startDate);
  const knownDays = totalsForMonth.filter(([, total]) => total > 0).length;
  const average = knownDays ? totalsForMonth.reduce((sum, [, total]) => sum + total, 0) / knownDays : null;

  elements.averageIntake.textContent = average === null ? "—" : `${Math.round(average).toLocaleString("fr-FR")} kcal`;
  elements.trackedDays.textContent = `sur ${knownDays} jour${knownDays > 1 ? "s" : ""} avec repas notés`;
  const monthlyWorkoutCalories = Object.entries(workouts)
    .filter(([day]) => day >= firstDay && day <= lastDay)
    .reduce((sum, [day, workout]) => sum + workoutCalories(workout, day), 0);
  const averageTarget = Math.round(profile.target + monthlyWorkoutCalories / monthDays(month));
  elements.dailyTarget.textContent = `${averageTarget.toLocaleString("fr-FR")} kcal`;
  if (!completeForMonth.length) {
    elements.monthlyChange.textContent = "—";
    elements.monthlyChangeNote.textContent = "Aucune journée complète pour estimer une tendance.";
  } else {
    const energyBalance = completeForMonth.reduce((sum, [day, intake]) => sum + expenditureForDay(day) - intake, 0);
    const change = energyBalance / 7700;
    const magnitude = Math.abs(change).toFixed(2).replace(".", ",");
    const changeLabel = change > 0.005 ? "perdus" : change < -0.005 ? "pris" : "estimés";
    elements.monthlyChange.textContent = `≈ ${magnitude} kg ${changeLabel}`;
    elements.monthlyChangeNote.textContent = `${completeForMonth.length} journée${completeForMonth.length > 1 ? "s" : ""} complète${completeForMonth.length > 1 ? "s" : ""} · modèle théorique`;
  }

  const actualWeights = Object.entries(weighIns)
    .filter(([day, weight]) => day >= firstDay && day <= lastDay && Number.isFinite(weight))
    .sort(([dayA], [dayB]) => dayA.localeCompare(dayB));
  if (actualWeights.length >= 2) {
    const measuredChange = actualWeights[actualWeights.length - 1][1] - actualWeights[0][1];
    const sign = measuredChange > 0 ? "+" : "";
    elements.monthlyChangeNote.textContent += ` · pesées réelles : ${sign}${measuredChange.toFixed(1).replace(".", ",")} kg`;
  }

  renderCalorieChart(month, dailyTotals);
  renderWeightChart(month, dailyTotals);
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
  renderReport();
}

function openProfileDialog() {
  elements.profileError.textContent = "";
  if (profile) {
    document.querySelector("#profile-age").value = profile.age;
    document.querySelector("#profile-sex").value = profile.sex;
    document.querySelector("#profile-height").value = profile.height;
    document.querySelector("#profile-weight").value = profile.weight;
    document.querySelector("#profile-activity").value = String(profile.activity);
  } else {
    elements.profileForm.reset();
  }
  elements.profileDialog.showModal();
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
  const index = Number(input.dataset.quantity);
  if (!Number.isFinite(grams) || grams <= 0 || grams > 10000 || !meal.items[index]) return;
  meal.items[index].grams = grams;
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

elements.mealDay.addEventListener("change", () => {
  if (!elements.mealDay.value) return;
  meal.date = elements.mealDay.value;
  renderMeal();
});

elements.clearButton.addEventListener("click", () => {
  meal = { id: null, name: "", date: meal.date, items: [] };
  renderMeal();
  showToast("Votre assiette a été vidée.");
});

elements.saveButton.addEventListener("click", () => {
  if (!meal.items.length) return;
  const existingEntry = meal.id ? history.find(entry => entry.id === meal.id) : null;
  const entry = {
    id: meal.id || (crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random()}`),
    name: meal.name.trim() || "Mon repas",
    date: new Date(`${meal.date}T12:00:00`).toISOString(),
    day: meal.date,
    total: Math.round(caloriesForItems(meal.items)),
    items: meal.items.map(item => ({ ...item }))
  };
  const nextHistory = existingEntry
    ? history.map(item => item.id === entry.id ? entry : item)
    : [entry, ...history];
  if (saveStorage(keys.history, nextHistory)) {
    history = nextHistory;
    const daysToReopen = new Set([entry.day]);
    if (existingEntry) daysToReopen.add(entryDay(existingEntry));
    const nextCompleted = completedDays.filter(day => !daysToReopen.has(day));
    if (nextCompleted.length !== completedDays.length) {
      if (saveStorage(keys.completedDays, nextCompleted)) completedDays = nextCompleted;
    }
    meal = { id: null, name: "", date: entry.day, items: [] };
    renderMeal();
    renderHistory();
    renderReport();
    showToast("Repas enregistré dans votre journal.");
  }
});

elements.completeDayButton.addEventListener("click", () => {
  if (!profile || caloriesForDay(meal.date) <= 0) return;
  const nextCompleted = completedDays.includes(meal.date)
    ? completedDays.filter(day => day !== meal.date)
    : [...completedDays, meal.date];
  if (saveStorage(keys.completedDays, nextCompleted)) {
    completedDays = nextCompleted;
    renderMeal();
    renderReport();
    showToast(completedDays.includes(meal.date) ? "Journée marquée comme complète." : "Journée réouverte.");
  }
});

elements.history.addEventListener("click", event => {
  const openButton = event.target.closest("[data-open-history]");
  const deleteButton = event.target.closest("[data-delete-history]");
  if (openButton) {
    const entry = history[Number(openButton.dataset.openHistory)];
    if (!entry) return;
    meal = { id: entry.id, name: entry.name, date: entryDay(entry), items: (entry.items || []).map(item => ({ ...item })) };
    renderMeal();
    selectTab(document.querySelector("#tab-meals-button"));
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
  if (deleteButton) {
    const deletedEntry = history[Number(deleteButton.dataset.deleteHistory)];
    const nextHistory = history.filter((_, index) => index !== Number(deleteButton.dataset.deleteHistory));
    if (saveStorage(keys.history, nextHistory)) {
      history = nextHistory;
      const deletedDay = deletedEntry ? entryDay(deletedEntry) : null;
      if (deletedEntry && meal.id === deletedEntry.id) {
        meal = { id: null, name: "", date: deletedDay || meal.date, items: [] };
      }
      if (deletedDay && completedDays.includes(deletedDay)) {
        const nextCompleted = completedDays.filter(day => day !== deletedDay);
        if (saveStorage(keys.completedDays, nextCompleted)) completedDays = nextCompleted;
      }
      renderHistory();
      renderMeal();
      renderReport();
    }
  }
});

document.querySelector("#profile-button").addEventListener("click", openProfileDialog);
document.querySelector("#profile-edit-button").addEventListener("click", openProfileDialog);
document.querySelector("[data-close-profile]").addEventListener("click", () => elements.profileDialog.close());
elements.profileDialog.addEventListener("click", event => {
  if (event.target === elements.profileDialog) elements.profileDialog.close();
});

elements.profileForm.addEventListener("submit", event => {
  event.preventDefault();
  const data = {
    age: Number(document.querySelector("#profile-age").value),
    sex: document.querySelector("#profile-sex").value,
    height: Number(document.querySelector("#profile-height").value),
    weight: Number(document.querySelector("#profile-weight").value),
    activity: Number(document.querySelector("#profile-activity").value)
  };
  if (data.age < 18 || data.age > 100 || data.height < 120 || data.height > 230 || data.weight < 30 || data.weight > 300) {
    elements.profileError.textContent = "Vérifiez l’âge, la taille et le poids saisis.";
    return;
  }
  const isFirstProfile = !profile;
  const calculated = calculateProfile(data);
  const nextProfile = {
    ...calculated,
    startWeight: isFirstProfile ? data.weight : profile.startWeight,
    startDate: isFirstProfile ? today : profile.startDate
  };
  if (!saveStorage(keys.profile, nextProfile)) return;
  profile = nextProfile;
  if (isFirstProfile && !Object.prototype.hasOwnProperty.call(weighIns, today)) {
    const nextWeighIns = { ...weighIns, [today]: data.weight };
    if (saveStorage(keys.weighIns, nextWeighIns)) weighIns = nextWeighIns;
  }
  elements.profileDialog.close();
  renderReport();
  showToast("Profil enregistré sur cet appareil.");
});

elements.reportMonth.addEventListener("change", renderReport);

elements.workoutForm.addEventListener("change", event => {
  if (event.target.matches('[name="workout-status"]')) {
    renderWorkoutPreview();
  } else if (event.target === elements.workoutDate) {
    loadWorkoutForDate(elements.workoutDate.value);
  } else {
    renderWorkoutPreview();
  }
});

elements.workoutForm.addEventListener("input", renderWorkoutPreview);

elements.workoutForm.addEventListener("submit", event => {
  event.preventDefault();
  const day = elements.workoutDate.value;
  const status = elements.workoutForm.querySelector('[name="workout-status"]:checked').value;
  const nextWorkouts = { ...workouts };

  if (!day) {
    showToast("Choisissez une date pour la séance.");
    return;
  }

  if (status === "no") {
    delete nextWorkouts[day];
  } else {
    const workout = {
      type: elements.workoutType.value,
      duration: Number(elements.workoutDuration.value),
      met: Number(elements.workoutIntensity.value)
    };
    if (!["push", "pull", "abdo-jambe"].includes(workout.type) ||
        !Number.isInteger(workout.duration) || workout.duration < 10 || workout.duration > 240 ||
        ![3.5, 6].includes(workout.met)) {
      showToast("Vérifiez le type, la durée et l’intensité de la séance.");
      return;
    }
    nextWorkouts[day] = workout;
  }

  if (saveStorage(keys.workouts, nextWorkouts)) {
    workouts = nextWorkouts;
    renderWorkoutPreview();
    renderReport();
    showToast(status === "yes" ? "Séance de musculation enregistrée." : "Statut sans séance enregistré.");
  }
});

elements.stepsDate.addEventListener("change", () => {
  const savedCount = steps[elements.stepsDate.value];
  elements.stepsCount.value = savedCount === undefined ? "" : String(savedCount);
});

elements.stepsForm.addEventListener("submit", event => {
  event.preventDefault();
  const day = elements.stepsDate.value;
  const count = Number(elements.stepsCount.value);
  const goal = Number(elements.stepsGoal.value);
  if (!day || !Number.isInteger(count) || count < 0 || count > 200000 ||
      !Number.isInteger(goal) || goal < 1000 || goal > 100000) {
    showToast("Vérifiez la date, le nombre de pas et l’objectif saisis.");
    return;
  }

  const nextSteps = { ...steps, [day]: count };
  if (!saveStorage(keys.steps, nextSteps)) return;
  if (!saveStorage(keys.stepsGoal, goal)) return;
  steps = nextSteps;
  stepsGoal = goal;
  renderStepsReport();
  showToast("Nombre de pas enregistré.");
});

elements.weighInForm.addEventListener("submit", event => {
  event.preventDefault();
  const day = elements.weighInDate.value;
  const weight = Number(elements.weighInWeight.value);
  if (!day || !Number.isFinite(weight) || weight < 20 || weight > 500) {
    showToast("Saisissez une date et un poids valide.");
    return;
  }
  const nextWeighIns = { ...weighIns, [day]: weight };
  if (saveStorage(keys.weighIns, nextWeighIns)) {
    weighIns = nextWeighIns;
    elements.weighInWeight.value = "";
    renderReport();
    showToast("Pesée enregistrée.");
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
  const nextFoods = [...customFoods, food];
  if (!saveStorage(keys.foods, nextFoods)) return;
  customFoods = nextFoods;
  activeCategory = "Tout";
  elements.search.value = "";
  renderCategories();
  renderFoods();
  addFood(food);
  elements.dialog.close();
  showToast("Aliment ajouté à votre assiette et à vos aliments.");
});

document.addEventListener("keydown", event => {
  if (event.key === "/" && !["INPUT", "TEXTAREA", "SELECT"].includes(document.activeElement.tagName) && !elements.dialog.open && !elements.profileDialog.open) {
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

elements.reportMonth.value = today.slice(0, 7);
elements.mealDay.value = meal.date;
elements.weighInDate.value = today;
elements.workoutDate.value = today;
loadWorkoutForDate(today);
elements.stepsDate.value = today;
elements.stepsGoal.value = String(stepsGoal);
elements.stepsCount.value = steps[today] === undefined ? "" : String(steps[today]);
renderAll();

if ("serviceWorker" in navigator && location.protocol !== "file:") {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("./service-worker.js").catch(error => {
      console.error("L’application hors ligne n’a pas pu être activée.", error);
    });
  });
}
