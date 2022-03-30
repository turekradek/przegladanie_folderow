import os
import pandas as pd

def folder( sciezka = os.getcwd() ):
    obiekty = os.listdir(sciezka)
    obiekty.insert(0,".\\")
    # for obiekt in obiekty:
    #     sciezka_obiektu = os.path.join(sciezka,obiekt)
    return obiekty , sciezka

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


