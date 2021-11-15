with open("insultes.txt", "r") as fichier_insultes:
    insultes = fichier_insultes.read()
    insultes = insultes.split("\n")

with open("non_insultes.txt","r") as fichier_non_insultes:
    non_insultes = fichier_non_insultes.read().split("\n")

if __name__ == "main":
    print(insultes)
    print(type(insultes))
