import os

try :
    os.chdir("GUI")
except :
    try :
        os.chdir("insultedetector_s2_YoutubeCleaner/GUI")
    except :
        pass

from logging import error
from tkinter import *
from tkinter.font import BOLD, ITALIC
import webbrowser
import pyperclip as pc
from fonctions import traitement_entree

print("--------------------------------")
print(os.getcwd())

bg_color = '#262525'  # Couleur du background, gris foncé
error_text = "Veuillez rentrer une URL, une ID ou un nom de chaîne valide"
images_path = 'images/'


def chemin(path):
    return(images_path+path)


def remplace_entree(entree, text):
    """Cette fonction remplace le contenu de entrée par text"""
    entree.delete(0, END)
    entree.insert(0, text)


def button_pushed(label, text, type_entree):
    """Fonction appelée lorsque le bouton principal est pressé"""
    result = traitement_entree(text, type_entree)
    if result == False:
        label.configure(text=error_text)


####### CREATION FENÊTRE PRINCIPALE ##########
window = Tk()
window.title("YouTubeCleaner Pro")
window.geometry("1080x720")
window.iconbitmap(chemin('logo.ico'))
window.config(background=bg_color)
window.minsize(1080, 720)

####### CREATION DES FRAMES  #########
frame = Frame(window, bg=bg_color)
frame_entree_pc = Frame(frame, bg=bg_color)  # entrée et bouton "coller"

####### IMAGE ########
logo = PhotoImage(file=chemin('logo.png'))
panel = Label(frame, image=logo, bg=bg_color)
panel.pack(side=TOP)

####### TEXTE ########
label_title = Label(
    frame, text="Recherchez les informations d'une chaîne ou vidéo YouTube", font=("Courrier", 26), bg=bg_color, fg='white')
label_title.pack()

####### ENTREE #######
entree = Entry(frame_entree_pc, textvariable=StringVar(
    frame_entree_pc, value=pc.paste()), font=('Arial', 18, ITALIC), fg='#1F676E', bg='#D9DEDE')
entree.pack(side=TOP, fill=X)

####### RADIOBUTTON (CHOIX URL/VIDEO/CHAINE) #########
frame_radiobutton = Frame(frame)
type_entree = StringVar()
rb_url = Radiobutton(frame_radiobutton, text='URL', variable=type_entree, value='url', bg=bg_color, fg='pink',
                     font=('Courrier', 19), cursor='hand2', activebackground=bg_color, activeforeground='pink',
                     selectcolor=bg_color)
rb_video = Radiobutton(frame_radiobutton, text='Vidéo', variable=type_entree, value='video', bg=bg_color, fg='pink',
                       font=('Courrier', 19), cursor='hand2', activebackground=bg_color, activeforeground='pink',
                       selectcolor=bg_color)
rb_chaine = Radiobutton(frame_radiobutton, text='Chaîne', variable=type_entree, value='channel', bg=bg_color, fg='pink',
                        font=('Courrier', 19), cursor='hand2', activebackground=bg_color, activeforeground='pink',
                        selectcolor=bg_color)
rb_url.pack(side=LEFT)
rb_video.pack(side=LEFT)
rb_chaine.pack(side=RIGHT)
rb_url.select()
frame_radiobutton.pack(expand=YES)

####### BOUTON "COLLER" #######
logo_pc = PhotoImage(file=chemin('pc_logo.png'))
logo_pc = logo_pc.subsample(x=2, y=2)
bouton_pc = Button(frame_entree_pc, image=logo_pc, cursor='hand2', bg='#4E5354', relief='groove',
                   command=lambda: remplace_entree(entree, pc.paste()))
bouton_pc.pack(side=LEFT)


####### TEXTE ERREUR #######
error_text_label = Label(frame_entree_pc, text="", font=(
    "Courrier", 15), bg=bg_color, fg='red')
error_text_label.pack()


frame_entree_pc.pack(fill=X)

####### BOUTON DE DEMARRAGE #######
bouton = Button(frame, text="GO !", font=("Courrier", 20, BOLD),
                bg='red', fg='white',  height=1, width=10, cursor='hand2',
                command=lambda: button_pushed(error_text_label, entree.get(), type_entree.get()))
bouton.pack(expand=YES)


frame.pack(expand=YES)


####### BOUTON GITLAB #######
lien_gitlab = "https://gitlab-ovh-02.cloud.centralesupelec.fr/edouard.roby/insultedetector_s2_YouTubeCleaner"
image_gitlab = PhotoImage(file=chemin('gitlab-logo.png'))
bouton_gitlab = Button(window, cursor='hand2',
                       image=image_gitlab, command=lambda: webbrowser.open_new(lien_gitlab))
bouton_gitlab.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)


window.mainloop()  # affichage de la fenêtre
