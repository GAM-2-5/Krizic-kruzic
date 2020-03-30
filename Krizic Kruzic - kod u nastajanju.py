prvigr=input('Prvi igrač\n')
druigr=input('Drugi igrač\n')
def krizic_kruzic():
    polje = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                              #polje - lista
    end = False
    pobj_kombinacije = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
 
    def cijelo_polje():                                                                      # polje - elementi iz liste
        print(polje[0], polje[1], polje[2])
        print(polje[3], polje[4], polje[5])
        print(polje[6], polje[7], polje[8])


 

 
    if input("Počni opet (da/ne)\n") == "da":
        print()
        krizic_kruzic()
 
krizic_kruzic()
