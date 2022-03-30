import os
def usuwanie_pustych_folderow():
    gdzie = os.getcwd()
    lista = os.listdir(gdzie)
    lista_pustych_folderow = []
    if 'foldery_puste.txt' not in lista:
        print( 'plik nie istnieje ')
    else:
        print( f' plik istnieje :)')
        with open('foldery_puste.txt','r') as puste_foldery:
            # sciezki = [ linia.strip() for linia in puste_foldery ]
            for linia in puste_foldery:
                linia = linia.strip()
                os.rmdir(linia)



usuwanie_pustych_folderow()
