from tkinter import *
from tkinter import filedialog

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.nomFichier1 = StringVar()
        self.nomFichier2 = StringVar()
        self.geometry("700x300")
        self.creer_widgets()

    def creer_widgets(self):
        
        self.frame1 = Frame(self)
        self.nomFichier1.set("fichier du Robot #1 ???")
        self.label1 = Label(self.frame1, textvariable=self.nomFichier1,fg="white", bg="red" )
        self.frame2 = Frame(self)
        self.nomFichier2.set("fichier du Robot #2 ???")
        self.label2 = Label(self.frame2, textvariable=self.nomFichier2,fg="white", bg="red" )
        self.bouton1 = Button(self.frame1, text="ouvrir", command=self.choixFichier1)
        self.bouton2 = Button(self.frame2, text="ouvrir", command=self.choixFichier2)
        
        
        self.label1.pack(side="left")
        self.bouton1.pack(side="right")
        self.label2.pack(side="left")
        self.bouton2.pack(side="right")
        self.frame1.pack(side="top")
        self.frame2.pack(side="top")
        self.frame3 = Frame(self)
        self.bouttonAppliquer = Button(self.frame3, text="Charger", command=self.setFiles,state = DISABLED)
        self.boutonQuitter= Button(self.frame3, text="Quitter", command=self.destroy)
        self.bouttonAppliquer.pack(side="left")
        self.boutonQuitter.pack(side = "right")
         
        self.frame3.pack(side="bottom")
        
    def choixFichier1(self):
        self.nomFichier1.set(filedialog.askopenfilename(filetypes =[('Python Files', '*.py')]))
        if self.nomFichier1.get() == "":
            self.label1.config(fg="white", bg="red")
            self.nomFichier1.set("fichier du Robot #1 ???")
            self.bouttonAppliquer.config(state = DISABLED)
        else :
            self.label1.config(fg="white", bg="green")
        if self.nomFichier1.get() != "fichier du Robot #1 ???" and self.nomFichier2.get() != "fichier du Robot #2 ???":
            self.bouttonAppliquer.config(state = NORMAL)
            
    def choixFichier2(self):
        self.nomFichier2.set(filedialog.askopenfilename(filetypes =[('Python Files', '*.py')]))
        if self.nomFichier2.get() == "":
            self.label2.config(fg="white", bg="red")
            self.nomFichier2.set("fichier du Robot #2 ???")
            self.bouttonAppliquer.config(state = DISABLED)
        else :
            self.label2.config(fg="white", bg="green")
        if self.nomFichier1.get() != "fichier du Robot #1 ???" and self.nomFichier2.get() != "fichier du Robot #2 ???":
            self.bouttonAppliquer.config(state = NORMAL)
    def setFiles(self):
        Application.setFile(1,self.nomFichier1.get())
        Application.setFile(2,self.nomFichier2.get())
        
    def setFile(num,nomFicBot):
        nomFichier = "IA"+str(num)+".py"
        f=open(nomFichier,"w")
        fia=open(nomFicBot,"r")
        for l in fia:
            f.write(l)
        f.close()
        fia.close()

if __name__ == "__main__":
    app = Application()
    app.title("Selection des Robots")
    app.mainloop()
        