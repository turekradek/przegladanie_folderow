import os
foldery = os.listdir()
print( foldery )
input()
for el in foldery:
    print( el )
    #if input('czy skasowac ')=='t':
    #    os.remove(el)
    if input('czy skasowac ')=='t':
        os.rmdir(el)
 
foldery = os.listdir()
print( foldery ) 
input('koniec')
