import os

def folder( sciezka , gdzie_jestem = os.getcwd()):
    obiekty = os.listdir(sciezka)

    for obiekt in obiekty:
        sciezka_obiektu = os.path.join(sciezka,obiekt)
        # WYSZUKUJE PLIKI Z - kopia W NAZWIE I ZAPISUEJ JE DO PLIKU pliki_kopia.txt
        # JEŚLI NIE MA W NAZWIE KOPIA A JEST TO PLIK ZAPISUJE SCIĘŻKĘ DO PLIKU pliki.txt
        # if os.path.isdir( sciezka_obiektu) == False:
        #     if '— kopia' in sciezka_obiektu:
        #         zapis_do_pliku('pliki_kopia.txt', sciezka_obiektu)
        #     else:
        #         zapis_do_pliku('pliki.txt',sciezka_obiektu )
        ############ WYŻEJ OPIS
        # ZNAJDUJE FOLDERY PUSTE W ŚRODKU I ZAPISUJE JE DO PLIKU foldery_puste.txt
        # POWINIEN BYĆ W KOMPLECIE PLIKU DO USUWANIA PUSTYCH FOLDERÓW
        # el ->
        if os.path.isdir( sciezka_obiektu) and len( os.listdir(sciezka_obiektu) )==0:
            zapis_do_pliku('foldery_puste.txt',gdzie_jestem ,sciezka_obiektu )

        elif os.path.isdir(sciezka_obiektu) :
            folder(sciezka_obiektu)
        # KOD PONIŻEJ SZUKA TYLKO FOLDERÓW KTÓRE W NAZWIE MAJĄ -kopia  I ZAPISUJE JE DO PLIKU
        # elif os.path.isdir(sciezka_obiektu) :
        #     if '— kopia' in sciezka_obiektu:
        #         zapis_do_pliku('foldery_kopia.txt', sciezka_obiektu)
        #         folder(sciezka_obiektu)
        #     else:
        #         zapis_do_pliku('foldery.txt',sciezka_obiektu)
        #         folder(sciezka_obiektu)

def foldery_kopia( sciezka , gdzie_jestem = os.getcwd()):
    obiekty = os.listdir(sciezka)
    for obiekt in obiekty:
        sciezka_obiektu = os.path.join(sciezka,obiekt)
        if os.path.isdir( sciezka_obiektu) == False:
            if '— kopia' in sciezka_obiektu:
                zapis_do_pliku('pliki_kopia.txt'  , gdzie_jestem , sciezka_obiektu)
        elif os.path.isdir( sciezka_obiektu ):
            if '— kopia' in sciezka_obiektu:
                zapis_do_pliku('foldery_kopia.txt', gdzie_jestem , sciezka_obiektu)
                foldery_kopia(sciezka_obiektu)
            else:
                foldery_kopia(sciezka_obiektu)

def zapis_do_pliku(plik,gdzie_zapisac, tekst):
    plik = os.path.join(gdzie_zapisac,plik)
    file = open( plik, 'a')
    file.write(tekst + '\n')
    file.close()


# print( ".\\")
foldery_kopia('E:\!!!!__programowanie__\!!!___git_projekty\!portfolio\przegladanie_folderow')