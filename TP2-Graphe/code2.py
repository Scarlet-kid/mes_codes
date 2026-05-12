import tkinter as tk
from tkinter import ttk, messagebox
import time

class PomodoroApp:
    """Application graphique pour la gestion des sessions Pomodoro."""
    
    # --- Constantes de temps (en secondes) ---
    WORK_TIME = 25 * 60
    SHORT_BREAK = 5 * 60
    LONG_BREAK = 15 * 60

    def __init__(self, master):
        """Initialisation de l'application et de l'interface graphique."""
        self.master = master
        master.title("🍅 Pomodoro Timer - Études Focus")
        master.geometry("400x300")
        master.resizable(False, False) # Empêche la redimensionnement

        # --- Variables d'état ---
        self.is_running = False
        self.time_remaining = self.WORK_TIME
        self.current_phase = "Travail" # Peut être : Travail, Court Break, Long Break
        
        # Création des widgets principaux
        self.setup_gui()

    def setup_gui(self):
        """Configure tous les éléments visuels de l'interface."""
        
        main_frame = ttk.Frame(self.master, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # 1. Affichage du temps (Label principal)
        self.time_label = tk.Label(
            main_frame, 
            text="25:00", 
            font=("Helvetica", 80, "bold"), 
            pady=20,
            fg="#E74C3C" # Couleur de fond rouge/orange
        )
        self.time_label.grid(row=0, column=0)

        # 2. Indicateur du mode actuel (Label secondaire)
        self.phase_label = tk.Label(
            main_frame, 
            text="Prêt pour la session de travail !", 
            font=("Helvetica", 16),
            pady=10
        )
        self.phase_label.grid(row=1, column=0)

        # 3. Boutons de contrôle
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0)

        self.start_btn = ttk.Button(button_frame, text="▶️ Commencer", command=self.start_timer)
        self.start_btn.grid(row=0, column=0, padx=10)

        self.pause_btn = ttk.Button(button_frame, text="⏸️ Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_btn.grid(row=0, column=1, padx=10)
        
        self.reset_btn = ttk.Button(button_frame, text="🔄 Réinitialiser", command=self.reset_timer)
        self.reset_btn.grid(row=0, column=2, padx=10)

    # ----------------- LOGIQUE DU TEMPORISATEUR -----------------

    def format_time(self, seconds):
        """Convertit les secondes en format MM:SS."""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def update_timer(self):
        """Fonction appelée chaque seconde pour décrémenter le temps."""
        if not self.is_running or self.time_remaining <= 0:
            return # Arrête si la session est terminée ou en pause

        # Décrémentation du temps
        self.time_remaining -= 1
        
        # Mise à jour de l'affichage
        self.time_label.config(text=self.format_time(self.time_remaining))
        
        # Vérification si le temps est écoulé
        if self.time_remaining <= 0:
            self.session_finished()
            return

        # Planifie l'appel de cette fonction dans 1000 millisecondes (1 seconde)
        self.master.after(1000, self.update_timer)


    def start_timer(self):
        """Démarrage du compte à rebours."""
        if not self.is_running:
            self.is_running = True
            # Désactiver le bouton Start et activer Pause
            self.start_btn.config(state=tk.DISABLED)
            self.pause_btn.config(state=tk.NORMAL)
            self.update_timer()

    def pause_timer(self):
        """Mise en pause du compte à rebours."""
        if self.is_running:
            self.is_running = False
            self.start_btn.config(text="▶️ Reprendre") # Change le texte pour l'utilisateur
            # Note : L'arrêt de la boucle est géré par la vérification dans update_timer

    def reset_timer(self):
        """Réinitialisation complète du timer à son état initial (Travail)."""
        self.is_running = False
        self.time_remaining = self.WORK_TIME
        
        # Mise à jour de l'affichage et des états
        self.time_label.config(text=self.format_time(self.WORK_TIME))
        self.phase_label.config(text="Prêt pour la session de travail !")
        self.start_btn.config(state=tk.NORMAL, text="▶️ Commencer")
        self.pause_btn.config(state=tk.DISABLED)

    def session_finished(self):
        """Gère les actions après l'écoulement total du temps."""
        self.is_running = False
        messagebox.showinfo("🎉 Fin de Session", f"Le temps est écoulé ! Votre phase actuelle ({self.current_phase}) est terminée.")
        
        # Logique de changement de phase (Cycle Pomodoro)
        if self.current_phase == "Travail":
            self.current_phase = "Court Break"
            self.time_remaining = self.SHORT_BREAK
            self.phase_label.config(text="✅ Courte pause ! Prenez un répit de 5 minutes.")
        elif self.current_phase == "Court Break":
            self.current_phase = "Travail"
            self.time_remaining = self.WORK_TIME
            self.phase_label.config(text="🚀 Reprise du travail ! C'est reparti pour 25 minutes.")
        else: # Si c'était le Long Break
            # Le cycle recommence en Travail, mais on fait une petite pause de confirmation
            messagebox.showinfo("Cycle Terminé", "🎉 Vous avez terminé un grand cycle de Pomodoro ! Reposez-vous bien.")
            self.current_phase = "Travail"
            self.time_remaining = self.WORK_TIME
            self.phase_label.config(text="✨ Cycle terminé. Prêt pour le prochain bloc !")

        # Réinitialise l'affichage après le changement de phase, sans relancer la boucle immédiatement
        self.reset_timer() 


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    # Initialisation : Assure que le timer est bien au démarrage sur le travail
    app.time_label.config(text=app.format_time(app.WORK_TIME)) 
    root.mainloop()
