#### Ciągi znaków (string)

str1 = "To jest string" # <--- staramy się unikania skrótu str, bo można pomylić z str()

s1 = "To jest zdanie."
s2 = """A to jest drugie zdanie"""

s = s1 + s2
print(s)

print(s1 + s2)

# zamiana zmiennych
s1 = "To jest to zdanie."
print(s1)

# czytelność 120 znaków
s3 = "To jest zdanie. Jest to długe zdanie," \
     "ktore tutaj wpisałem" \
     "a które podzieliłem by było to czytelniejsze. Nie powinno przekraczać 120 znaków"

s4 = 'inny sposób'

s5 = """A to jest "cytat"."""
s6 = '''tak jest lepiej "cytat"'''

s7 = "To jest pierwsza linia \n To jest druga linia"
print(s7)

# Funkcja print
z1 = "przykład"
print("To jest przykład")
print(f"To jest {z1}")  #  fstring
print("To jest {}".format(z1))
print("To jest {}. {}".format("przykład", "a to jest dodatek"))
print("To jest {0}. {1}".format("przykład", "a to jest dodatek"))

print("to", " jest", " przykład")
print("to" + " jest" + "przykład")
#Funkcja str()

p1 = "to jest zdanie"
print(type(p1))

licz1 = 33
print(licz1)
print(type(licz1))

tmp1 = str(licz1)
print("to jest: ",tmp1)
print(type(tmp1))