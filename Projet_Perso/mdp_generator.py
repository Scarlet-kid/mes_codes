import string
import random 
import tkinter as tk
from tkinter import messagebox

def generer_password(longeur):
    all = string.digits + string.ascii_letters
    #all = string.printable
    var = ""
    for i in range(longeur):
        var += random.choice(all)
    return var

#print(generer_password(12))
def generer():
    try : 
        zone_sortie.delete("1.0",tk.END)
        longueur = entry1.get()
        if not longueur:
            messagebox.showwarning("Attention","Veuillez entrer la longueur de mdp souhaité!")
            return
        nombre = int(longueur)
        zone_sortie.insert(tk.END,generer_password(nombre))
    except ValueError:
        messagebox.showwarning("Erreur"," La longueur doit etre un entier !")
    
def copier():
    text_a_copier = zone_sortie.get("1.0",tk.END).strip()
    if not text_a_copier:
        messagebox.showwarning("Vide","RIen a copier")
        return
    
    fen.clipboard_clear()
    fen.clipboard_append(text_a_copier)
    fen.update()
    messagebox.showinfo("Réussite","Copier avec succès dans le presse-papier")

fen = tk.Tk()
fen.title("G2nérateur de mdp")

text1 = tk.Label(fen,text="Entrez la longueur du mot de passe : ")
text1.pack(pady=5)

entry1 = tk.Entry(fen)
entry1.pack(pady=5)

btn = tk.Button(fen,text='Générer',command=generer)
btn.pack()

zone_sortie = tk.Text(fen,height=10,width=50,bg='white')
zone_sortie.pack(pady=10)

btn_quitter  = tk.Button(fen,text="quitter",command=fen.destroy,bg='red',fg='white')
btn_quitter.pack()

btn_copier = tk.Button(fen,text="Copier",command=copier)
btn_copier.pack()

fen.mainloop()