import tkinter as tk
from tkinter import messagebox
import psycopg2

def envoyer_donnees():
    nom = entry_nom.get()
    email = entry_email.get()
    
    if not nom or not email:
        messagebox.showwarning("Attention, tous les champs sont obligatoires.")
        return
    
    try:
        connection = psycopg2.connect(
            host = "localhost",
            database = "postgres",
            user = "postgres",
            password = "66793270"
        )
        cursor = connection.cursor()
        query = "INSERT INTO utilisateurs (nom, email) VALUES (%s, %s)"
        data = (nom,email)
        cursor.execute(query,data)
        connection.commit()
        messagebox.showinfo("Succès","Les données ont été enregistrée avec succès")
        entry_nom.delete(0,tk.END)
        entry_email.delete(0,tk.END)
        
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur de connexion : {e}")
    finally:
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()

root = tk.Tk()
root.title("Mon formulaire")
root.geometry("300x250")
label_nom = tk.Label(root,text="Nom :")
label_nom.pack(pady=5)
entry_nom = tk.Entry(root)
entry_nom.pack(pady=5)

label_email = tk.Label(root,text="email")
label_email.pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

btn = tk.Button(root,text="Enregistrer",command=envoyer_donnees)
btn.pack(pady=20)

btn_quit = tk.Button(root,text="quitter",command=root.destroy,bg='red',fg='white')
btn_quit.pack(pady=5)
root.mainloop()