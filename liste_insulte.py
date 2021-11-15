with open("insultes.txt", "r") as fichier_insultes:
    insultes = fichier_insultes.read()
    insultes = insultes.split("\n")

print(insultes)
print(type(insultes))
