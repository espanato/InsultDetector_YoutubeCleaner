with open("insultes.txt", "r", encoding="utf-8") as fichier_insultes:
    insultes = fichier_insultes.read()
    insultes = insultes.split("\n")

# print(insultes)
# print(type(insultes))

with open("non_insultes.txt", "r", encoding="utf-8") as fichier_non_insultes:
    non_insultes = fichier_non_insultes.read().split("\n")

if __name__ == "main":
    print(insultes)
    print(type(insultes))
