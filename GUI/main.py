from tkinter import *
import webbrowser
import pyperclip as pc
from fonctions import reconnait_lien

bg_color = '#262525'


def remplace_entree(entree, text):
    """Cette fonction remplace le contenue de entrée par text"""
    entree.delete(0, END)
    entree.insert(0, text)


window = Tk()

window.title("YoutubeCleaner Pro")
window.geometry("1080x720")
window.iconbitmap("GUI/logo.ico")
window.config(background=bg_color)


frame = Frame(window, bg=bg_color)
logo = PhotoImage(file="GUI/logo.png")
panel = Label(frame, image=logo)
panel.pack(side=TOP)
frame_entree_pc = Frame(frame, bg=bg_color)

label_title = Label(
    frame, text="Rentrez l'url d'une vidéo ou d'une chaîne Youtube", font=("Courrier", 26), bg=bg_color, fg='white')
label_title.pack()

entree = Entry(frame_entree_pc, textvariable=StringVar(
    frame_entree_pc, value=pc.paste()), font=('Arial', 18))
entree.pack(side=TOP, fill=X)

logo_pc = PhotoImage(file="GUI/pc_logo.png")
logo_pc = logo_pc.subsample(x=2, y=2)
bouton_pc = Button(frame_entree_pc, image=logo_pc,
                   command=lambda: remplace_entree(entree, pc.paste()))
bouton_pc.pack(side=LEFT)


frame_entree_pc.pack(fill=X)


photo = PhotoImage(file="GUI/logo.png")
bouton = Button(frame, text="GO !", font=("Courrier", 20),
                bg='red', fg='white',  height=1, width=10, command=lambda: reconnait_lien(entree.get()))
bouton.pack(expand=YES)


frame.pack(expand=YES)


# GITLAB_BUTTON

lien_gitlab = "https://gitlab-ovh-02.cloud.centralesupelec.fr/edouard.roby/insultedetector_s2_YouTubeCleaner"
image_gitlab = PhotoImage(file="GUI/gitlab-logo.png")


def ouvrir_lien_gitlab():
    webbrowser.open_new(lien_gitlab)


bouton_gitlab = Button(window, text="Pouii",
                       image=image_gitlab, command=ouvrir_lien_gitlab)
bouton_gitlab.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

window.mainloop()


print("yes")
