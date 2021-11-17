from fonctions import reconnait_lien
import pyperclip as pc
import webbrowser
from tkinter.font import ITALIC
from tkinter import *
from logging import error
import os

fin = os.getcwd().split("\\")[-1]
if fin != "GUI":
    os.chdir("GUI")
# os.system("pause")


bg_color = '#262525'  # Couleur du background, gris foncé
error_text = "Veuillez rentrer une URL, une ID ou un nom de chaîne valide"


def remplace_entree(entree, text):
    """Cette fonction remplace le contenu de entrée par text"""
    entree.delete(0, END)
    entree.insert(0, text)


def affiche_error_text(label, text):
    if reconnait_lien(text) == False:
        label.configure(text=error_text)


####### CREATION FENÊTRE PRINCIPALE ##########
window = Tk()
window.title("YoutubeCleaner Pro")
window.geometry("1080x720")
window.iconbitmap("images/logo.ico")
window.config(background=bg_color)
window.minsize(1080, 720)

####### CREATION DES FRAMES  #########
frame = Frame(window, bg=bg_color)
frame_entree_pc = Frame(frame, bg=bg_color)  # entrée et bouton "coller"

####### IMAGE ########
logo = PhotoImage(file="images/logo.png")
panel = Label(frame, image=logo)
panel.pack(side=TOP)

####### TEXTE ########
label_title = Label(
    frame, text="Rentrez l'url d'une vidéo ou d'une chaîne Youtube", font=("Courrier", 26), bg=bg_color, fg='white')
label_title.pack()

####### ENTREE #######
entree = Entry(frame_entree_pc, textvariable=StringVar(
    frame_entree_pc, value=pc.paste()), font=('Arial', 18, ITALIC), fg='#1F676E')
entree.pack(side=TOP, fill=X)

####### BOUTON "COLLER" #######
logo_pc = PhotoImage(file="images/pc_logo.png")
logo_pc = logo_pc.subsample(x=2, y=2)
bouton_pc = Button(frame_entree_pc, image=logo_pc,
                   command=lambda: remplace_entree(entree, pc.paste()))
bouton_pc.pack(side=LEFT)

####### TEXTE ERREUR #######
error_text_label = Label(frame_entree_pc, text="", font=(
    "Courrier", 15), bg=bg_color, fg='red')
error_text_label.pack()


frame_entree_pc.pack(fill=X)

####### BOUTON DE DEMARRAGE #######
bouton = Button(frame, text="GO !", font=("Courrier", 20),
                bg='red', fg='white',  height=1, width=10, command=lambda: affiche_error_text(error_text_label, entree.get()))
bouton.pack(expand=YES)


frame.pack(expand=YES)


####### BOUTON GITLAB #######
lien_gitlab = "https://gitlab-ovh-02.cloud.centralesupelec.fr/edouard.roby/insultedetector_s2_YouTubeCleaner"
image_gitlab = PhotoImage(file="images/gitlab-logo.png")
bouton_gitlab = Button(window, text="Pouii",
                       image=image_gitlab, command=lambda: webbrowser.open_new(lien_gitlab))
bouton_gitlab.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)


window.mainloop()  # affichage de la fenêtre
