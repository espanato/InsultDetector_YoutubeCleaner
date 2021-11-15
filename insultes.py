liste_insultes = ["connard","salope"]

def levenshtein(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(levenshtein(a[1:], b[1:])+(a[0] != b[0]),
               levenshtein(a[1:], b)+1,
               levenshtein(a, b[1:])+1)
    
print(levenshtein("cat","chello"))


def est_insulte(mot):
    for ins in liste_insultes :
        if levenshtein(mot,ins) <= 1 :
            return True
        else :
            return False





"""
arbre = {}
def ajoute_mot(mot,arbre):
    if len(mot) == 1 :
        arbre[mot[0]] = True
    else :
        ajoute_mot(mot[0:],arbre[mot[0]])

ajoute_mot("connard",arbre)
"""
def est_insulte(mot):
        