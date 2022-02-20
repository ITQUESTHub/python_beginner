#### Liczby ####

# Liczby całkowite (int)

liczba1 = 10
liczba2 = 5

suma = liczba1 + liczba2
print(suma)

suma2 = liczba2 + 30
print(suma2)

# Liczby rzeczywiste (zmiennoprzecinkowe)
zm1 = 3.14
zm2 = 6.2456

suma = zm1 + zm2
print(suma)

zm3 = 5.12345678910
print(zm3)

#zawężąnie do miejsc po przecinku - zaokrąglanie
print("%.2f" % zm3)
print("%.4f" % zm3)

#inny sposób format()
print("{:.3f}".format(zm3))

#f-strings
print(f'{zm3:.5f}')

# zaokrąglanie rount()
tmp = round(zm3, 4)
print(tmp)

#Funkcja int()
a = "13"
b= int(a)
print(b)
print(type(b))

#funkcja float()
a = 13
b = float(b)
print(b)
print(type(b))

# przy działaniach Python rozpoznaje co ma zrobić ze zmiennymi
a = 120
b = 10.55
suma = a + b
print(suma)
