from tkinter import *
import webbrowser
bg_color = '#262525'


window = Tk()

window.title("YoutubeCleaner Pro")
window.geometry("1080x720")
window.iconbitmap("GUI/logo.ico")
window.config(background=bg_color)

frame = Frame(window, bg=bg_color)


label_title = Label(
    frame, text="Rentrez l'url d'une vidéo ou d'une chaîne Youtube", font=("Courrier", 26), bg=bg_color, fg='white')
label_title.pack()

entree = Entry(frame, textvariable="URL")
entree.pack(fill=X)


def print_entree():
    print(entree.get())


photo = PhotoImage(file="GUI/logo.png")
bouton = Button(frame, text="GO !", font=("Courrier", 20),
                bg='red', fg='white',  height=1, width=10, default='active', command=print_entree)
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
