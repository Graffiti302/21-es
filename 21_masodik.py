import random
from random import randint

print("Üdvözöllek a 21-es játékban!!")
print("A játék célja, hogy 21 legyen a számok összege.")
print("Két számot kapsz 1-10-ig. Késöbb több számot is Kérhetsz.")
print("Ha túllépsz a 21-es számon akkor vesztettél!")
print("Kezdjük el!")
print("----------------------------------------")
def AI_game():
    szamok = [random.randint(1, 10, ), random.randint(1, 10)]
    jatekosok = str(input("Hányan játszotok? Gép/egyedül:"))
    if jatekosok == "Gép":
        print(f"Az első számod:{szamok[0]}")
        print(f"A második számod: {szamok[1]}")

    def summa():
        szam_osszeg = sum(szamok)
        print(f"A számaid összege:{szam_osszeg}")
    summa()

    def kartya_keres():
        Valasztas = str(input("Ha kérsz még egy kártyát írj <Igen> ha nem akkor <Nem>"))
        if Valasztas != "Igen" or "Nem":
            print("Ez nem választási lehetőség")
        if Valasztas == "Igen":
            print("Akkor kapsz még kártyát!")
        szamok.append(random.randint(1, 10))
        print(f"A következő számod:{szamok[2]}")
        summa()
        ellenorzes()
        kartya_keres()
        if Valasztas == "Nem":
            gép()



    def ellenorzes():
        if sum(szamok) == 21:
         print("Nyertél")
        elif sum(szamok) > 21:
            print("Vesztettél!")
            Ujra = str(input("Akarsz újra játszani? Y/N:"))
            if Ujra == "Y":
                AI_game()

    kartya_keres()
    def gép():
        Gép_szamok = [random.randint(1, 10),random.randint(1,10)]


        def gép_ellenőrzés():
            if Gép_szamok < 16:
                gép_plus()
            Gép_osszeg = sum(Gép_szamok)
            if Gép_osszeg < 16:
                gép_plus()


        def gép_plus():
            Gép_szamok.append(random.randint(1, 10))
            gép_summa()


        def gép_summa():
            Gép_osszeg = sum(Gép_szamok)
            gép_ellenőrzés()
        gép_ellenőrzés()






AI_game()









def gép():
        Gép_szamok = [random.randint(1, 10),random.randint(1,10)]

        def gép_plus():
            Gép_szamok.append(random.randint(1,10))
            gép_summa()

        def gép_ellenőrzés():
            if Gép_szamok < 16:
                gép_plus()


        def gép_summa():
            Gép_osszeg = sum(Gép_szamok)
            gép_ellenőrzés()
        gép_ellenőrzés()
