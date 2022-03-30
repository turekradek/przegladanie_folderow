import os

def folder( sciezka ):

    obiekty = os.listdir(sciezka)
    for obiekt in obiekty:
        sciezka_obiektu = os.path.join(sciezka,obiekt)
        if os.path.isdir( sciezka_obiektu) == False:
            zapis_do_pliku('pliki.txt',sciezka_obiektu )
        elif os.path.isdir( sciezka_obiektu) and len( os.listdir(sciezka_obiektu) )==0:
            zapis_do_pliku('foldery_puste.txt',sciezka_obiektu )
        elif os.path.isdir(sciezka_obiektu) :
            zapis_do_pliku('foldery.txt',sciezka_obiektu)
            folder(sciezka_obiektu)


def zapis_do_pliku(plik, tekst):
    file = open( plik, 'a')
    file.write(tekst + '\n')
    file.close()



razem = folder( os.getcwd() )

with open('foldery.txt','r') as foldery, open('pliki.txt','r') as pliki, open('foldery_puste.txt','r') as foldery_puste, open('duplikaty.txt','w') as duplikaty:
    fold = foldery.readlines()
    fold_puste = foldery_puste.readlines()
    pli = pliki.readlines()

for el in fold:
    print( el )

# filename, file_extension = os.path.splitext('/path/to/somefile.ext')

# — kopia.


