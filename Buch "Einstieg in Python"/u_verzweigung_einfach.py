#Eingabe
print("Geben Sie ihr Bruttogehalt in Euro ein:")

gehaltseingabe = input()
gehalt = int(gehaltseingabe)

#Berechnung

if gehalt >= 2500:
    print("Es ergibt sich folgender Steuerbetrag:", (gehalt*22)/100, "Euro")

else:
    print("Es ergibt sich folgender Steuerbetrag:", (gehalt*18)/100, "Euro")