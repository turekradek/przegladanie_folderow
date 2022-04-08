import os
import pandas as pd

def folder( sciezka = os.getcwd() ):
    obiekty = os.listdir(sciezka)
    obiekty.insert(0,".\\")
    # for obiekt in obiekty:
    #     sciezka_obiektu = os.path.join(sciezka,obiekt)
    return obiekty , sciezka

def folder_w_glab( sciezka = os.getcwd() ):
    obiekty = os.listdir( sciezka )
    for obiekt in obiekty:
        if os.path.isdir( obiekt ):
            folder_w_glab(os.path.abspath( obiekt ) )

def szukaj_kopia( sciezka = os.getcwd() ):
    obiekty = os.listdir(sciezka)
    kopia = 'kopia'
    # zapis na pulpicie

    # przeszukaj dysk c i zapisz na pulpicie jeœli nie znajdziesz w tej lokalizacji
    print( f'F szukaj_kopii sciezka do pbiektu {sciezka}, obiekty {obiekty} , kopia w sciezka ',kopia in sciezka )
    for obiekt in obiekty:
        # print( f'\tfunkcja szukaj_kopia {obiekt}')
        cala_sciezka = os.path.join(sciezka,obiekt)
        print( f'\tPRZED IF kopia i obiekt {kopia}, {obiekt}', kopia in obiekt , type(obiekt), 'cala sciezka',cala_sciezka)

        if kopia in cala_sciezka:
            gdzie_apka = os.path.abspath('apka.py')
            zapis_folder = 'E:\!!!!__programowanie__\!!!___git_projekty\!portfolio\przegladanie_folderow'
            zapis_plik = 'obiekty_z_kopia_w_nazwie.txt'
            calosc = os.path.join(zapis_folder,zapis_plik)
            zapis_do_pliku(calosc, f'{cala_sciezka}')
            # print(f'\t\tPO IF kopia i obiekt {kopia}, {obiekt}', kopia in obiekt, type(obiekt), 'cala sciezka', cala_sciezka)



        if os.path.isdir(obiekt):
            sciezka_ = os.path.abspath( obiekt )
            # print(f'\t\t REKURENCJA IF kopia i obiekt {kopia}, {obiekt}', kopia in obiekt, type(obiekt), 'cala sciezka',
            #   cala_sciezka)
            # print(f'\t \tfunkcja szukaj_kopia {obiekt} i jego sciezka_{sciezka_}')
            szukaj_kopia(sciezka_)


def trescfolderu( sciezka ):
    obiekty = os.listdir( sciezka )
    obiekty = '\n'.join(obiekty)
    return obiekty

def trescpliku( sciezka ):
    with open( sciezka ,'r') as plik:
        tresc = plik.read()
    return tresc

def policz_pliki(sciezka):
    obiekty =  [ obiekt  for obiekt in os.listdir(sciezka) if os.path.isdir(obiekt) == False ]
    return len(obiekty)

def policz_foldery(sciezka):
    obiekty =  [ obiekt  for obiekt in os.listdir(sciezka) if os.path.isdir( os.path.join( sciezka, obiekt))]
    return len( obiekty )

def zapis_do_pliku(plik, tekst):
    file = open( plik, 'a')
    file.write(tekst + '\n')
    file.close()

def get_disks():
    '''create list of disks on Windows for ThisPC folder'''
    names = []
    for s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        disk = '%s:' % s
        if os.path.isdir(disk):
            names.append(disk)
    return names

# dyski = get_disks()
# print( dyski )
# with open('dyski.txt','w') as dyski_:
#     lista = []
#     for dysk in dyski:
#         dyski_.write(30 * ' *')
#         dyski_.write('\n')
#         dyski_.write(dysk)
#         dyski_.write('\n')
#         dyski_.write('\n'.join( os.listdir(dysk)))


# zapis_do_pliku('aaa.txt','druga linia ')