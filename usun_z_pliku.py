import os
import shutil
# shutil.rmtree('/folder_name')
import znajdz_puste_foldery
def usuwanie( plik):
    gdzie = os.getcwd()
    print( f'gdzie {gdzie} ' )
    lista = os.listdir(gdzie)
    print(   f'lista {lista} ')
    print( 'A TERAZ GDZIE JESTEM ')
    gdzie = znajdz_puste_foldery.lokalizacja_aplikacji
    plik_z_pustymi_folderami_do_skasowania = os.path.join(gdzie,plik)
    lista2 = os.listdir(gdzie )
    print( f'A TERAZ  gdzie {gdzie} ' )
    # print( f'A TERAZ  lista {lista2} ')
    if plik not in lista2:
        print( f'{plik} nie istnieje ')
    else:

        print( f'{plik_z_pustymi_folderami_do_skasowania}  istnieje :)')
        with open(plik_z_pustymi_folderami_do_skasowania,'r') as puste_foldery:
            # sciezki = [ linia.strip() for linia in puste_foldery ]
            for linia in puste_foldery:
                linia = linia.strip()
                if os.path.exists( linia ):
                    os.rmdir(linia)
                else:
                    print( f'folder lub plik {linia} nie istnieje')

def usuwanie_kopia( plik ):
    gdzie = os.getcwd()
    lista = os.listdir(gdzie)
    if plik not in lista:
        print( f'{plik} nie istnieje ')
    else:
        print( f'{plik}  istnieje :)')
        with open(plik,'r') as puste_foldery:
            # sciezki = [ linia.strip() for linia in puste_foldery ]
            for linia in puste_foldery:
                linia = linia.strip()
                if os.path.exists( linia ):
                    lista_aktualnego = os.listdir(linia)
                    print( f'folder {linia} zawiera nastepujace elementy \n {lista_aktualnego}')
                    if input('Czy mam usunac caly folder t=tak,  n=nie ').lower() == 't':
                        shutil.rmtree( linia)
                        # os.rmdir(linia)
                else:
                    print( f'folder lub plik {linia} nie istnieje')

def usuwanie_pliki_kopia( plik ):
    gdzie = os.getcwd()
    lista = os.listdir(gdzie)
    if plik not in lista:
        print( f'{plik} nie istnieje ')
    else:
        print( f'{plik}  istnieje :)')
        with open(plik,'r') as puste_foldery:
            # sciezki = [ linia.strip() for linia in puste_foldery ]
            for linia in puste_foldery:
                linia = linia.strip()
                if os.path.exists(linia) and os.path.isdir( linia ) != True:
                    os.remove(linia)
                else:
                    print( f'folder lub plik {linia} nie istnieje')

