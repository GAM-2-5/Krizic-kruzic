def krizic_kruzic():
    prvigr=input('Prvi igrač\n')                                                    #prvi igrač unese ime
    druigr=input('Drugi igrač\n')                                                 #drugi igrač unese ime
    polje = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                             #polje - lista
    kraj = False                                                                             #kasnije nam treba kraj, 'nije kraj'
    pobj_kombinacije = ((0, 1, 2), (6, 7, 8), (3, 4, 5), (1, 4, 7), (2, 5, 8), (0, 3, 6), (0, 4, 8), (2, 4, 6))
 
    def cijelo_polje():                                                                      # polje - elementi iz liste
        print(polje[0], polje[1], polje[2])                                          #prikaz polja
        print(polje[3], polje[4], polje[5])
        print(polje[6], polje[7], polje[8])
        print()                                                                                     #prazna crta za bolji pregled u igri

    def odabir():                                                                              #definiran odabir 

    def igr1():                                                                                 #definiran prvi igrač
        n = odabir()                                                                          #bira polje
        if polje[n] == "X" or polje[n] == "O":                                  #ako je polje promijenjeno iz broja u X ili O, ...
            print("\nOvo je polje zauzeto!")                                      #... ispisuje da je zauzeto
        else:                                                                                     #ako nije, ...
            polje[n] = "X"                                                                   #... za prvog igrača piše X
 
    def igr2():                                                                                 #definiran drugi igrač
        n = odabir()                                                                          #bira polje
        if polje[n] == "X" or polje[n] == "O":                                  #ako je polje promijenjeno iz broja u X ili O, ...
            print("\nOvo je polje zauzeto!")                                      #... ispisuje da je zauzeto
        else:                                                                                     #ako nije, ...
            polje[n] = "O"                                                                   #... za drugog igrača piše O

    def provjeravanje():                                                                    #ovo ću još promijeniti
        brojač = 0
        for a in pobj_kombinacije:
            if polje[a[0]] == polje[a[1]] == polje[a[2]] == "X":
                print(prvigr.upper()," je pobijedio!\n")
                return True
 
            if polje[a[0]] == polje[a[1]] == polje[a[2]] == "O":
                print(druigr.upper()," je pobijedio!\n")
                return True
        for a in range(9):
            if polje[a] == "X" or polje[a] == "O":
                brojač += 1
            if brojač == 9:
                print("Izjednačeno je!\n")
                return True
 
 
    if input("Počni opet (da/ne)\n") == "da":                               #opet početi?
        print()
        krizic_kruzic()
 
krizic_kruzic()
