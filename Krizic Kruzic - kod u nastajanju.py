def krizic_kruzic():
    prvigr=input('Prvi igrač\n')
    druigr=input('Drugi igrač\n')
    polje = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                              #polje - lista
    kraj = False
    pobj_kombinacije = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
 
    def cijelo_polje():                                                                      # polje - elementi iz liste
        print(polje[0], polje[1], polje[2])
        print(polje[3], polje[4], polje[5])
        print(polje[6], polje[7], polje[8])
        print()                                                                                     #prazna crta za bolji pregled u igri

    def igr1():
        n = odabir()
        if polje[n] == "X" or polje[n] == "O":
            print("\nOvo je polje zauzeto!")
            igr1()
        else:
            polje[n] = "X"
 
    def igr2():
        n = odabir()
        if polje[n] == "X" or polje[n] == "O":
            print("\nOvo je polje zauzeto!")
            igr2()
        else:
            polje[n] = "O"

    def odabir():

    def provjeravanje():
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
 
    while not kraj:
        cijelo_polje()
        kraj = provjeravanje()
        if kraj == True:
            break
        print(prvigr.upper(), " stavlja križić!")
        igr1()
        print()
        cijelo_polje()
        kraj = provjeravanje()
        if kraj == True:
            break
        print(druigr.upper(), " stavlja kružić!")
        igr2()
        print()
 
    if input("Počni opet (da/ne)\n") == "da":
        print()
        krizic_kruzic()
 
krizic_kruzic()
