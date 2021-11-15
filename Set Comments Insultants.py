import keyboard
import codecs
import time
from search_comments import dico_en_3

dic1, dic2, dic3 = dico_en_3('TRY2eQju5nc', '5r-ZsKH3uNE', '6janW0h3cZY', 3)
print('Prêt à commencer !')
for k, v in dic3.items():
    i = 1
    c = 0
    print(v)
    time.sleep(2)
    while c == 0:
        if keyboard.is_pressed('i'):
            file = codecs.open('./Commentaires insultants/' +
                               'Commentaire '+str(k)+'.txt', 'w', encoding='utf-8')
            file.write(v)
            c = 1
        elif keyboard.is_pressed('n'):
            file = codecs.open('./Commentaires neutres/' +
                               'Commentaire '+str(k)+'.txt', 'w', encoding='utf-8')
            file.write(v)
            c = 2
    if c == 1:
        print(f'Le commentaire {k} est insultant')
    elif c == 2:
        print(f"Le commentaire {k} n'est pas insultant")
    i += 1
