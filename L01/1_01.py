### Wprowadzenie do zmiennych ###

#### Jak nazywać zmienne

zmienna1 = "Zmienna powinna zacyznać się od litery!"
zmiennaDruga2 = "Zmienna może korzystać ze znaków alfabetu oraz cyfr"
Zmienna2Druga = "jw."
To_jest_zmienna = "Zamiast spacji, używaj podkreślenia"
_zmienna = "Zmienna może w niektórych wypadkach zaczynać się od podkreślnika"


# niepoprawne!
3dsa = "Zmienna nie może na poczatku mieć cyfry!"
>zmienna = "zmienna nie powinna posiadać innych znaków specjalnych"
-niepoprawna_zmienna = "jw."
Zmienna! = "zmienna nie może zawierać znaków specjalnych"
Zm!enna = "jw."
ZmiennaJestCaseSensitive = "Uwaga na wielkość liter! Zmienna1, zmienna1, zmieNNa1 to trzy różne zmienne"
str = "unikamy nazw funkcji wykorzystywanych w pythonie"

# Przypisywanie kilku zmiennych na raz
z1, z2, z3 = "słowo1", "słowo2", 110

#### Komentarze ####

# komentarz
text1 = "to jest przykład" #Tutaj wpisujemy komentarz

# To jest przykład sumy
suma1 = 25 + 100

"""To jest przukład 
komentarza który jest
wielolinijkowy"""

#To jest przykład komentarza, która jest jednoczesnie opisem funkcji
def funkcja(x=1, y=3):
    """To jest funcja sumująca dwie liczby"""
    print (x+y)

#### Ciągi znaków (string) ####
text = 'To jest przykładowy string"'
text2 = "PASSWORD123!@#$"
text3 = """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
        dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
        commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id 
        est laborum.
        """

#### Liczby całkowite (int) ####

num1 = 10100
num2 = 35
sum = num1 + num2

#### Liczby zmiennoprzecinkowe / rzeczywiste (float) ####

x = 100,23
y = 77,34567
pi = 3,1415926

#### Listy (list) ####

list1 = ["Pies", "Kot", "Papuga", "Kaczka"]
list2 = [1, 55, 130, 5500]
lsit3 = ["Pies", 1, 71, "Samochód", "Samolot"]

#### Krotki (tuples) ####

krotka1 = (1, 2, 33, 67, 151)
krotka2 = ("pomidor", "marchewka", "ogórek", "fasolka", "por")
krotka3 = ("liczba1", 354, 1199, "liczba4", "liczba5")

#### Słowniki (dictionary) ####

dict1 = {
    "pierwsz litera":   "A",
    "druga litera":     "B",
    "trzecia litera":   "C"
        }

dict2 = {
    "pierwsza zienna":  1100,
    "druga zmienna":    77,
    "trzecia zmienna":  "Ciąg_znaków",
    "czwarta zmienna":  553
        }


#### Typ logiczny (Bool)

prawda = True
falsz = False

if prawda is True:
    print("prawda")
else:
    print("fałsz")

### funkcja print (wyświetl)

z1 = "przykład"
print(z1)


# To na kiedyś !
print("To jest przykład")
print(f"To jest {z1}")
print("To jest {}".format(z1))