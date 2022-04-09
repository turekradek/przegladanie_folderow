import os
def usuwanie_pustych_folderow( plik ):
    gdzie = os.getcwd()
    lista = os.listdir(gdzie)
    lista_pustych_folderow = []
    if plik not in lista:
        print( f'{plik} nie istnieje ')
    else:
        print( f'{plik}  istnieje :)')
        with open(plik,'r') as puste_foldery:
            # sciezki = [ linia.strip() for linia in puste_foldery ]
            for linia in puste_foldery:
                linia = linia.strip()
                os.rmdir(linia)



# usuwanie_pustych_folderow()
