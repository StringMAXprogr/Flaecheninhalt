import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

# Zeichnet ein Dreieck
def zeichne_dreieck(grundlinie, hoehe, farbe="lime", hintergrund="black"):
    fig, ax = plt.subplots()
    ax.set_facecolor(hintergrund)
    ax.plot([0, grundlinie, grundlinie / 2, 0], [0, 0, hoehe, 0], color=farbe, linewidth=2)
    ax.set_xlim(-1, grundlinie + 1)
    ax.set_ylim(-1, hoehe + 1)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(color="green", linestyle="--", linewidth=0.5)
    plt.title("Dreieck")
    plt.show()

# Zeichnet ein Rechteck
def zeichne_rechteck(laenge, breite, farbe="lime", hintergrund="black"):
    fig, ax = plt.subplots()
    ax.set_facecolor(hintergrund)
    ax.plot([0, laenge, laenge, 0, 0], [0, 0, breite, breite, 0], color=farbe, linewidth=2)
    ax.set_xlim(-1, laenge + 1)
    ax.set_ylim(-1, breite + 1)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(color="green", linestyle="--", linewidth=0.5)
    plt.title("Rechteck")
    plt.show()

# Zeichnet ein Quadrat
def zeichne_quadrat(seitenlaenge, farbe="lime", hintergrund="black"):
    zeichne_rechteck(seitenlaenge, seitenlaenge, farbe, hintergrund)

# Zeichnet eine Raute
def zeichne_raute(diagonale_e, diagonale_f, farbe="lime", hintergrund="black"):
    fig, ax = plt.subplots()
    ax.set_facecolor(hintergrund)
    ax.plot([0, diagonale_e / 2, 0, -diagonale_e / 2, 0], [diagonale_f / 2, 0, -diagonale_f / 2, 0, diagonale_f / 2], color=farbe, linewidth=2)
    ax.set_xlim(-diagonale_e, diagonale_e)
    ax.set_ylim(-diagonale_f, diagonale_f)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(color="green", linestyle="--", linewidth=0.5)
    plt.title("Raute")
    plt.show()

# Zeichnet ein Trapez
def zeichne_trapez(a, c, h, farbe="lime", hintergrund="black"):
    fig, ax = plt.subplots()
    ax.set_facecolor(hintergrund)
    ax.plot([0, a, c, 0], [0, 0, h, h], color=farbe, linewidth=2)
    ax.set_xlim(-1, max(a, c) + 1)
    ax.set_ylim(-1, h + 1)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(color="green", linestyle="--", linewidth=0.5)
    plt.title("Trapez")
    plt.show()

# Zeichnet ein Deltoid
def zeichne_deltoid(diagonale_e, diagonale_f, farbe="lime", hintergrund="black"):
    fig, ax = plt.subplots()
    ax.set_facecolor(hintergrund)
    ax.plot(
        [0, diagonale_e / 2, 0, -diagonale_e / 2, 0],
        [diagonale_f / 2, 0, -diagonale_f / 2, 0, diagonale_f / 2],
        color=farbe,
        linewidth=2,
    )
    ax.set_xlim(-diagonale_e, diagonale_e)
    ax.set_ylim(-diagonale_f, diagonale_f)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(color="green", linestyle="--", linewidth=0.5)
    plt.title("Deltoid")
    plt.show()

# GUI für Dreieck
def dreieck_gui():
    def berechnen():
        try:
            grundlinie = float(entry_grundlinie.get())
            hoehe = float(entry_hoehe.get())
            if grundlinie <= 0 or hoehe <= 0:
                raise ValueError
            flaecheninhalt = (grundlinie * hoehe) / 2
            messagebox.showinfo("Ergebnis", f"Flächeninhalt: {flaecheninhalt:.2f} cm²")
            zeichne_dreieck(grundlinie, hoehe)
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben.")

    fenster = tk.Tk()
    fenster.title("Dreieck")
    fenster.geometry("400x300")

    tk.Label(fenster, text="Grundlinie (cm):").pack(pady=5)
    entry_grundlinie = tk.Entry(fenster)
    entry_grundlinie.pack(pady=5)

    tk.Label(fenster, text="Höhe (cm):").pack(pady=5)
    entry_hoehe = tk.Entry(fenster)
    entry_hoehe.pack(pady=5)

    tk.Button(fenster, text="Berechnen und Zeichnen", command=berechnen).pack(pady=20)
    fenster.mainloop()

# GUI für Rechteck
def rechteck_gui():
    def berechnen():
        try:
            laenge = float(entry_laenge.get())
            breite = float(entry_breite.get())
            if laenge <= 0 or breite <= 0:
                raise ValueError
            flaecheninhalt = laenge * breite
            messagebox.showinfo("Ergebnis", f"Flächeninhalt: {flaecheninhalt:.2f} cm²")
            zeichne_rechteck(laenge, breite)
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben.")

    fenster = tk.Tk()
    fenster.title("Rechteck")
    fenster.geometry("400x300")

    tk.Label(fenster, text="Länge (cm):").pack(pady=5)
    entry_laenge = tk.Entry(fenster)
    entry_laenge.pack(pady=5)

    tk.Label(fenster, text="Breite (cm):").pack(pady=5)
    entry_breite = tk.Entry(fenster)
    entry_breite.pack(pady=5)

    tk.Button(fenster, text="Berechnen und Zeichnen", command=berechnen).pack(pady=20)
    fenster.mainloop()

# GUI für Quadrat
def quadrat_gui():
    def berechnen():
        try:
            seitenlaenge = float(entry_seitenlaenge.get())
            if seitenlaenge <= 0:
                raise ValueError
            flaecheninhalt = seitenlaenge ** 2
            messagebox.showinfo("Ergebnis", f"Flächeninhalt: {flaecheninhalt:.2f} cm²")
            zeichne_quadrat(seitenlaenge)
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben.")

    fenster = tk.Tk()
    fenster.title("Quadrat")
    fenster.geometry("400x300")

    tk.Label(fenster, text="Seitenlänge (cm):").pack(pady=5)
    entry_seitenlaenge = tk.Entry(fenster)
    entry_seitenlaenge.pack(pady=5)

    tk.Button(fenster, text="Berechnen und Zeichnen", command=berechnen).pack(pady=20)
    fenster.mainloop()

# GUI für Raute
def raute_gui():
    def berechnen():
        try:
            diagonale_e = float(entry_diagonale_e.get())
            diagonale_f = float(entry_diagonale_f.get())
            if diagonale_e <= 0 or diagonale_f <= 0:
                raise ValueError
            flaecheninhalt = (diagonale_e * diagonale_f) / 2
            messagebox.showinfo("Ergebnis", f"Flächeninhalt: {flaecheninhalt:.2f} cm²")
            zeichne_raute(diagonale_e, diagonale_f)
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben.")

    fenster = tk.Tk()
    fenster.title("Raute")
    fenster.geometry("400x300")

    tk.Label(fenster, text="Diagonale e (cm):").pack(pady=5)
    entry_diagonale_e = tk.Entry(fenster)
    entry_diagonale_e.pack(pady=5)

    tk.Label(fenster, text="Diagonale f (cm):").pack(pady=5)
    entry_diagonale_f = tk.Entry(fenster)
    entry_diagonale_f.pack(pady=5)

    tk.Button(fenster, text="Berechnen und Zeichnen", command=berechnen).pack(pady=20)
    fenster.mainloop()

# GUI für Trapez
def trapez_gui():
    def berechnen():
        try:
            a = float(entry_a.get())
            c = float(entry_c.get())
            h = float(entry_h.get())
            if a <= 0 or c <= 0 or h <= 0:
                raise ValueError
            flaecheninhalt = ((a + c) * h) / 2
            messagebox.showinfo("Ergebnis", f"Flächeninhalt: {flaecheninhalt:.2f} cm²")
            zeichne_trapez(a, c, h)
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben.")

    fenster = tk.Tk()
    fenster.title("Trapez")
    fenster.geometry("400x300")

    tk.Label(fenster, text="Obere Basis a (cm):").pack(pady=5)
    entry_a = tk.Entry(fenster)
    entry_a.pack(pady=5)

    tk.Label(fenster, text="Untere Basis c (cm):").pack(pady=5)
    entry_c = tk.Entry(fenster)
    entry_c.pack(pady=5)

    tk.Label(fenster, text="Höhe h (cm):").pack(pady=5)
    entry_h = tk.Entry(fenster)
    entry_h.pack(pady=5)

    tk.Button(fenster, text="Berechnen und Zeichnen", command=berechnen).pack(pady=20)
    fenster.mainloop()

# GUI für Deltoid
def deltoid_gui():
    def berechnen():
        try:
            diagonale_e = float(entry_diagonale_e.get())
            diagonale_f = float(entry_diagonale_f.get())
            if diagonale_e <= 0 or diagonale_f <= 0:
                raise ValueError
            flaecheninhalt = (diagonale_e * diagonale_f) / 2
            messagebox.showinfo("Ergebnis", f"Flächeninhalt: {flaecheninhalt:.2f} cm²")
            zeichne_deltoid(diagonale_e, diagonale_f)
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben.")

    fenster = tk.Tk()
    fenster.title("Deltoid")
    fenster.geometry("400x300")

    tk.Label(fenster, text="Diagonale e (cm):").pack(pady=5)
    entry_diagonale_e = tk.Entry(fenster)
    entry_diagonale_e.pack(pady=5)

    tk.Label(fenster, text="Diagonale f (cm):").pack(pady=5)
    entry_diagonale_f = tk.Entry(fenster)
    entry_diagonale_f.pack(pady=5)

    tk.Button(fenster, text="Berechnen und Zeichnen", command=berechnen).pack(pady=20)
    fenster.mainloop()

# Hauptmenü
def berechne_flaecheninhalt_gui():
    def weiter():
        auswahl = auswahl_var.get()
        if auswahl == "Dreieck":
            dreieck_gui()
        elif auswahl == "Rechteck":
            rechteck_gui()
        elif auswahl == "Quadrat":
            quadrat_gui()
        elif auswahl == "Raute":
            raute_gui()
        elif auswahl == "Trapez":
            trapez_gui()
        elif auswahl == "Deltoid":
            deltoid_gui()

    root = tk.Tk()
    root.title("Flächeninhalt Berechnung")
    root.geometry("400x250")

    tk.Label(root, text="Wähle eine Form aus:", font=("Arial", 14)).pack(pady=10)
    auswahl_var = tk.StringVar(value="Dreieck")
    dropdown = ttk.Combobox(root, textvariable=auswahl_var, values=["Dreieck", "Rechteck", "Quadrat", "Raute", "Trapez", "Deltoid"], state="readonly")
    dropdown.pack(pady=10)

    tk.Button(root, text="Weiter", command=weiter, width=20).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    berechne_flaecheninhalt_gui()