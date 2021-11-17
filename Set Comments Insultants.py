import keyboard
import codecs
import time
from search_comments import collect_comments_and_replies

dic1= collect_comments_and_replies('QbrNKOQMahk', 100)
print('Prêt à commencer !')
for k, v in dic1.items():
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
