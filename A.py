import time

print("Hier kannst du den Flächeninhalt eines Vierecks berechnen!")
time.sleep(1)

# Schleife, die den Benutzer auffordert, Enter zu drücken
while True:
    eingabe = input("Drücke Enter, um fortzufahren: ")
    if eingabe == "":
        break
    else:
        print("Bitte drücke nur die Enter-Taste.")

# Schleife für die Auswahl der Vierecksart
while True:
    print("\nGib bitte folgende Werte ein:")
    art = input("Art des Vierecks (Rechteck, Quadrat, Raute, Paralellogramm, Trapez, Deltoid) oder 'exit' zum Beenden: ").strip().lower()
    
    if art == "exit":
        print("Programm beendet. Auf Wiedersehen!")
        exit()
    elif art in ["rechteck", "quadrat", "raute", "paralellogramm", "trapez", "deltoid"]:
        break
    else:
        print("Ungültige Eingabe. Bitte wähle eine gültige Vierecksart.")

def berechne_flaecheninhalt_rechteck():
    """Berechnet den Flächeninhalt eines Rechtecks."""
    try:
        laenge = float(input("Länge (in cm): "))
        breite = float(input("Breite (in cm): "))
        if laenge <= 0 or breite <= 0:
            print("Länge und Breite müssen positive Zahlen sein.")
            return
        flaecheninhalt = laenge * breite
        print(f"Der Flächeninhalt des Rechtecks beträgt {flaecheninhalt:.2f} cm².")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie Zahlen ein.")

def berechne_flaecheninhalt_raute():
    """Berechnet den Flächeninhalt einer Raute."""
    try:
        e = float(input("Länge der Diagonale e (in cm): "))
        f = float(input("Länge der Diagonale f (in cm): "))
        if e <= 0 or f <= 0:
            print("Diagonalen müssen positive Zahlen sein.")
            return
        flaecheninhalt = (e * f) / 2
        print(f"Der Flächeninhalt der Raute beträgt {flaecheninhalt:.2f} cm².")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie Zahlen ein.")

def berechne_flaecheninhalt_trapez():
    """Berechnet den Flächeninhalt eines Trapezes."""
    try:
        a = float(input("Länge der oberen Basis a (in cm): "))
        c = float(input("Länge der unteren Basis c (in cm): "))
        h = float(input("Höhe h (in cm): "))
        if a <= 0 or c <= 0 or h <= 0:
            print("Basen und Höhe müssen positive Zahlen sein.")
            return
        flaecheninhalt = ((a + c) * h) / 2
        print(f"Der Flächeninhalt des Trapezes beträgt {flaecheninhalt:.2f} cm².")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie Zahlen ein.")

if art == "rechteck":
    berechne_flaecheninhalt_rechteck()
elif art == "raute":
    berechne_flaecheninhalt_raute()
elif art == "trapez":
    berechne_flaecheninhalt_trapez()
else:
    print("Diese Vierecksart wird noch nicht unterstützt.")
