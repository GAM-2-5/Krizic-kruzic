def krizic_kruzic():
    prvigr=input('Prvi igrač\n')                                                    #prvi igrač unese ime
    druigr=input('Drugi igrač\n')                                                 #drugi igrač unese ime
    polje = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                             #polje - lista
    kraj = False                                                                             #kasnije nam treba kraj, 'nije kraj'
    pobj_kombinacije = ((0, 1, 2), (6, 7, 8), (3, 4, 5), (1, 4, 7), (2, 5, 8), (0, 3, 6), (0, 4, 8), (2, 4, 6)) #pobjedničke kombinacije
 
    def cijelo_polje():                                                                      # polje - elementi iz liste
        print(polje[0], polje[1], polje[2])                                          #prikaz polja
        print(polje[3], polje[4], polje[5])                                          #prikaz polja
        print(polje[6], polje[7], polje[8])                                          #prikaz polja
        print()                                                                                     #prazna crta za bolji pregled u igri

    def odabir():                                                                              #definiran odabir 
        while True:                                                                             #dok je True
            while True:
                a = input()                                                                     #unosimo odabir
                try:                                                                                #provjeravamo ispravnost unesenog
                    a  = int(a)                                                                     #pretvaramo u int() - brojevnu vrijednost
                    a -= 1                                                                          #ovo je zbog lakšeg prepoznavanja
                    if a in range(0, 9):                                                    #ako je a od 0 do 9,
                        return a                                                                    #program ga vraća - ide dalje
                    else:                                                                               #ako nije broj od 0 do 9,
                        print("\nOvaj broj ne spada u ponuđenu listu!")      #piše da ne spada u te brojeve
                        continue
                except ValueError:                                                           #ValueError - nije broj jer je a int()
                   print("\nOvo nije broj!")                                                #isprinta da nije broj (inače bi javilo pogrešku)
                   continue                                                                       #nastavlja na slijedeći red
                
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

    def provjeravanje():                                                                  #definirano provjeravanje
        brojač = 0                                                                             #zadana vrijednost brojača
        for a in pobj_kombinacije:                                                  #ako je a u pojedničkim kombinacijama
            if polje[a[0]] == polje[a[1]] == polje[a[2]] == "X":            #ako su sve to isti simboli (u ovom slučaju X)
                print(prvigr.upper()," je pobijedio!\n")                            #prikaže poruku da je taj igrač pobijedio
                return True                                                                     #provjeravanje() je sada True
 
            if polje[a[0]] == polje[a[1]] == polje[a[2]] == "O":            #ako su sve to isti simboli (u ovom slučaju O)
                print(druigr.upper()," je pobijedio!\n")                            #prikaže poruku da je taj igrač pobijedio
                return True                                                                     #provjeravanje() je sada True
        for a in range(9):                                                                     #ako je a (9 puta)
            if polje[a] == "X" or polje[a] == "O":                                      #ako je na tom polju X ili O,
                brojač = brojač + 1                                                         #brojaču dodaje 1
            if brojač == 9:                                                                     #ako je brojač 9 (znači da su sva polja zauzeta i nije bilo pobj. kombinacije)
                print("Izjednačeno je!\n")                                               #kaže da je izjednačeno
                return True                                                                     #provjeravanje() je sada True

    while not kraj:                                                                             #dok nije kraj
        cijelo_polje()                                                                          #imamo cijelo polje - 'prizivamo' ga
        kraj = provjeravanje()                                                            #kraj je jednak provjeravanju
        if kraj == True:                                                                        #ako je kraj (provjeravanje()) True
            break                                                                                   #idemo na kraj
        print(prvigr.upper(), " stavlja križić!")                                       #kaže poruku
        igr1()                                                                                      #prizivamo prvog igrača
        print()                                                                                     #linija za preglednost
        cijelo_polje()                                                                           #opet prizivamo cijelo polje
        kraj = provjeravanje()                                                            #kraj je jednak provjeravanju
        if kraj == True:                                                                        #ako je kraj (provjeravanje()) True
            break                                                                                   #idemo na kraj
        print(druigr.upper(), " stavlja kružić!")                                       #kaže poruku
        igr2()                                                                                      #prizivamo drugog igrača
        print()                                                                                     #linija za preglednost
 
    if input("Počni opet (da/ne)\n") == "da":                               #opet početi?
        print()                                                                                     #linija je samo za razdvajanje igara (može ih biti i više)
        print()                                                                                     #isto
        krizic_kruzic()                                                                         #zatvorimo
 
krizic_kruzic()                                                                             #zatvorimo za kraj
