# Modul random importieren
import random

# Zufallsgenerator initiallisieren
random.seed()

# Zufallswerte und Berechnungen
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print("Die Aufgabe:", a, "+", b)

# Eingabe
print("Bitte eine Zahl eingeben:")
z = input()
zahl = int(z)

# Ausgabe
print("Ihre Eingabe:", z)
print("Das Erbenis:", c)