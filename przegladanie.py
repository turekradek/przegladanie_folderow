import os

def folder( sciezka ):

    obiekty = os.listdir(sciezka)
    obiekty.insert(0,".\\")
    for obiekt in obiekty:
        sciezka_obiektu = os.path.join(sciezka,obiekt)
    return obiekty , sciezka

def trescfolderu( sciezka ):
    obiekty = os.listdir( sciezka )
    obiekty = '\n'.join(obiekty)
    return obiekty

def trescpliku( sciezka ):
    print( sciezka )
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




# print( policz_pliki(r'E:\!!!!__programowanie__\!!!___git_projekty\!portfolio\przegladanie_folderow'))
print( policz_foldery(r'E:\!!!!__programowanie__\!!!___git_projekty\!portfolio\przegladanie_folderow\a'))