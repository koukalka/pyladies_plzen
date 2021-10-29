# Funkce = poznamky k lekci pyladies.cz/plzen
# 26.10.2021

######### uvod #########
# co to je:
# - soubor prikazu (operaci)
# - priklad na obvodu kruhu (parametr, vzorecek, print)
# prakticky a laicky: chci uvarit polevku = funkce: uvar_polevku

# k cemu je dobra:
# - univerzalni
# - z kombinace x prikazu udela jeden
# - citelne

# funkce, ktere uz pouzili:
# - print
# - range
# - turtle - forward, left, right
# - matematika - round, sin, sqrt, abs, apod.
# - vstup - input()
# - datove typy - int()

print("Ahojky lidi")
print()

for i in range(0,10,2):
    print(i)
print()

from random import uniform, randrange
nahodne_cislo = uniform(0,20)
print(nahodne_cislo)
print()

from math import sqrt
sqrt(16)
print()

#prerusovana cara
from turtle import forward, left, penup, pendown, exitonclick
forward(10)
penup()
forward(10)
pendown()
forward(10)
print()
exitonclick()

######## co je treba vedet #########
# - definuje se pred pouzitim (stejne jako promenna)
# - vstupni parametry neboli argumenty funkce (priklady viz vyse)
# - existuji funkce, kdy parametry nepotrebuji a i tak neco delaji - u zelvy
# - nejprve funkci definuji a pak ji volam

# funkce, ktera nic nevrati - procedury
# - funkce mohou i nemusi nic vracet
# - funkce print - neco provede (provede operaci), ale nevraci nam nic
# - (napriklad vypise na obrazovku, zkopiruje soubor, spusti zvuk, zavre okno, kresli na obrazovku)
print()
print("AHOJ")
print("Ahoj svete mam se krasne", "a ty?", sep = ',', end ="\n")
print()
# - nekdy taky procedura
vypis = print("AHOJ")
print(vypis)
print()

# funkce, ktera neco vrati
# - funkce jako takova se ale pouziva, aby nam neco vratila
# - vysledek funkce muzeme ulozit do promenne, promenna bude obsahovat navratovou hodnotu
odmocnina = sqrt(361)
print(odmocnina)

# - funkce se musi volat, jinak se kod nespusti a nic se neprovede
# - rozdil mezi promennou a funkci je v () ... bez zavorek ji nezavolam a nespustim
nahodne_cele_cislo = randrange(0,20)
print(nahodne_cele_cislo)


######## syntaxe a tvorba vlastni funkce #########
# pomoci def

'''
def nazev_funkce (argumenty - pokud je potrebuji):
    telo funkce
    "popis funkce neni povinny"
    neco delej

    budto mi neco vrat, pak pisu return, a nebo taky nebo ne
    return neco (vrat mi neco)
'''

#zadefinovanou funkci potom muzeme volat
'''
nazev_funkce(argumenty - pokud je potrebuji)
'''

######## vlastni funkce bez parametru, nic nevracejici
import datetime as dt
# - knihovna datetime, objekt datetime a v nem funkce now()

def vypis_aktualni_cas():
    cas = dt.datetime.now()
    print(cas)

vypis_aktualni_cas()
aa = vypis_aktualni_cas()
print(aa)


########  vlastni funkce bez parametru, vrati hodnotu
# volne misto na disku C

def aktualni_cas():
    cas = dt.datetime.now()
    return cas

aktualni_cas()
aktu_cas = aktualni_cas()
print("Aktualni cas je tedka", aktu_cas)


########  vlastni funkce s parametry, nic nevracejici
from math import pi

def vypis_obvod_kruhu(polomer):
    obvod = 2 * polomer * pi
    print(obvod)

vypis_obvod_kruhu(4)
vypis_obvod_kruhu(4.6)
a = vypis_obvod_kruhu(4)
print(a)

########  vlastni funkce s parametry, vracejici
def obvod_kruhu(polomer):
    obvod = 2 * polomer * pi
    return obvod

obvod_kruhu(4)
obvod_je = obvod_kruhu(4)
obvod_je_zaokrouhleny = round(obvod_je)
print("Obvod kruhu je:", obvod_je_zaokrouhleny)

polomer = 2
obvod_kruhu(5)
print(polomer)


######## advanced ########

####### prazdna funkce
# - aby nevyhodila chybu, píše se pass
# - kdyz si chci predpripravit funkci, ale jeste ji neimplementuji (bude se hodit do budoucna, budu ji potrebovat - nacrtnu si ji)

'''
def prazdna_funkce():
#IndentationError
'''
def prazdna_funkce():
    pass


######## rekurzivni funkce
# - funkce volajici sama sebe
# - faktorial typicky, Fibonacciho posloupnost
# - 3 = 3*2*1
# - 4 = 4*3*2*1
# - trochu cyklus, ale bez pouziti while
# - musi byt podminka, kdy to skonci! - když je to 1 skonči
# - cykli se v sobe

def faktorial(cislo):
    if cislo > 1:
        faktorial_spoctu = cislo * faktorial(cislo-1)
        return faktorial_spoctu
    else:
        return 1


faktorial_je = faktorial(5)
print("Faktorial je",faktorial_je)
print("Faktorial je",faktorial(40))


##################### cviceni na konec #####################
# program, ktery se uzivatele pta na nejakou otazku (vstupni parametr otazky)
# neda mu pokoj (otazka se porad opakovala), dokud mu neodpovi ANO nebo NE

# minule while cyklus

# dneska z toho udelat funkci
# vstupni parametr pouzit (otazku)
# funkce vrati odpoved (ANO,NE)

otazka = "Máš mě rád?"

def ano_ne(otazka):

    while True:
        odpoved = input(otazka)

        if (odpoved == "ano") or (odpoved == "ne"):
            return odpoved

pom = ano_ne(otazka)
print(pom)

