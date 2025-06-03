import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

def zeichne_dreieck_aus_seiten(a, b, c, farbe="lime", hintergrund="white"):
    import numpy as np
    A = (0, 0)
    B = (c, 0)
    try:
        C_x = (b**2 + c**2 - a**2) / (2 * c)
        C_y = np.sqrt(b**2 - C_x**2)
    except Exception:
        messagebox.showerror("Fehler", "Ungültige Seitenlängen für ein Dreieck.")
        return
    fig, ax = plt.subplots()
    ax.set_facecolor(hintergrund)
    xs = [A[0], B[0], C_x, A[0]]
    ys = [A[1], B[1], C_y, A[1]]
    ax.plot(xs, ys, color=farbe, linewidth=2)
    ax.set_aspect("equal")
    plt.title("Dreieck")
    plt.show()

def zeichne_rechteck(a, b, farbe="lime", hintergrund="white"):
    fig, ax = plt.subplots()
    ax.set_facecolor(hintergrund)
    ax.plot([0, a, a, 0, 0], [0, 0, b, b, 0], color=farbe, linewidth=2)
    ax.set_aspect("equal")
    plt.title("Rechteck")
    plt.show()

def zeichne_quadrat(a, farbe="lime", hintergrund="white"):
    zeichne_rechteck(a, a, farbe, hintergrund)

def zeichne_raute(e, f, farbe="lime", hintergrund="white"):
    fig, ax = plt.subplots()
    ax.set_facecolor(hintergrund)
    ax.plot([0, e/2, 0, -e/2, 0], [f/2, 0, -f/2, 0, f/2], color=farbe, linewidth=2)
    ax.set_aspect("equal")
    plt.title("Raute")
    plt.show()

def zeichne_trapez_eindeutig(a, c, h, farbe="lime", hintergrund="white"):
    import numpy as np
    versatz = (c - a) / 2
    d = np.sqrt(versatz**2 + h**2)
    A = (0, 0)
    B = (a, 0)
    D = (c, h)
    C = (0, h)
    xs = [A[0], B[0], D[0], C[0], A[0]]
    ys = [A[1], B[1], D[1], C[1], A[1]]
    fig, ax = plt.subplots()
    ax.set_facecolor(hintergrund)
    ax.plot(xs, ys, color=farbe, linewidth=2)
    ax.set_aspect("equal")
    plt.title("Trapez")
    plt.show()

def zeichne_deltoid_eindeutig(a, c, e, farbe="lime", hintergrund="white"):
    import numpy as np
    # a = kurze Seite, c = lange Seite, e = Diagonale zwischen den kurzen Seiten
    # Wir berechnen die andere Diagonale f
    # Die Diagonalen stehen senkrecht aufeinander und halbieren sich gegenseitig
    # f = 2 * sqrt(a**2 - (e/2)**2)
    if e >= 2*a or e >= 2*c or a <= 0 or c <= 0 or e <= 0:
        messagebox.showerror("Fehler", "Kein Deltoid mit diesen Werten konstruierbar.")
        return
    try:
        f = 2 * np.sqrt(a**2 - (e/2)**2)
    except Exception:
        messagebox.showerror("Fehler", "Kein Deltoid mit diesen Werten konstruierbar.")
        return
    E1 = np.array([-e/2, 0])
    E2 = np.array([e/2, 0])
    F1 = np.array([0, f/2])
    F2 = np.array([0, -f/2])
    fig, ax = plt.subplots()
    ax.set_facecolor(hintergrund)
    xs = [E1[0], F1[0], E2[0], F2[0], E1[0]]
    ys = [E1[1], F1[1], E2[1], F2[1], E1[1]]
    ax.plot(xs, ys, color=farbe, linewidth=2)
    ax.set_aspect("equal")
    ax.annotate(f"a = {a:.2f}", ((E1[0]+F1[0])/2, (E1[1]+F1[1])/2), color="blue", fontsize=12)
    ax.annotate(f"c = {c:.2f}", ((E1[0]+F2[0])/2, (E1[1]+F2[1])/2), color="red", fontsize=12)
    ax.annotate(f"e = {e:.2f}", (0, 0.2), color="green", fontsize=12)
    ax.annotate(f"f = {f:.2f}", (0.2, 0), color="purple", fontsize=12)
    plt.title("Deltoid")
    plt.show()

def berechne_flaecheninhalt_gui():
    def zeige_eingabefelder(form):
        for widget in haupt_frame.winfo_children():
            widget.destroy()
        eingabefelder.clear()
        if form == "Dreieck":
            felder = [
                ("Seite a", 'a'),
                ("Seite b", 'b'),
                ("Seite c", 'c'),
            ]
        elif form == "Rechteck":
            felder = [
                ("Seite a", 'a'),
                ("Seite b", 'b'),
            ]
        elif form == "Quadrat":
            felder = [
                ("Seite a", 'a'),
            ]
        elif form == "Raute":
            felder = [
                ("Diagonale e", 'e'),
                ("Diagonale f", 'f'),
            ]
        elif form == "Trapez":
            felder = [
                ("Obere Basis a", 'a'),
                ("Untere Basis c", 'c'),
                ("Höhe h", 'h'),
            ]
        elif form == "Deltoid":
            felder = [
                ("Seite a", 'a'),
                ("Seite c", 'c'),
                ("Diagonale e", 'e'),
            ]
        else:
            felder = []
        for label_text, var in felder:
            lbl = tk.Label(haupt_frame, text=label_text, font=("Arial", 13), bg="#f7f7f7")
            lbl.pack(pady=(8,0))
            entry = tk.Entry(haupt_frame, font=("Arial", 13), width=18, bg="white")
            entry.pack(pady=(0,2))
            eingabefelder[var] = entry
        btn = tk.Button(haupt_frame, text="Berechnen & Zeichnen", command=berechnen, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), height=2, width=25)
        btn.pack(pady=18)

    def berechnen():
        form = auswahl_var.get()
        try:
            if form == "Dreieck":
                a = float(eingabefelder['a'].get())
                b = float(eingabefelder['b'].get())
                c = float(eingabefelder['c'].get())
                if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
                    raise ValueError
                s = (a + b + c) / 2
                flaecheninhalt = (s * (s - a) * (s - b) * (s - c)) ** 0.5
                ergebnis_feld.config(state="normal")
                ergebnis_feld.delete(0, tk.END)
                ergebnis_feld.insert(0, f"A = {flaecheninhalt:.2f}")
                ergebnis_feld.config(state="readonly")
                zeichne_dreieck_aus_seiten(a, b, c)
            elif form == "Rechteck":
                a = float(eingabefelder['a'].get())
                b = float(eingabefelder['b'].get())
                if a <= 0 or b <= 0:
                    raise ValueError
                flaecheninhalt = a * b
                ergebnis_feld.config(state="normal")
                ergebnis_feld.delete(0, tk.END)
                ergebnis_feld.insert(0, f"A = {flaecheninhalt:.2f}")
                ergebnis_feld.config(state="readonly")
                zeichne_rechteck(a, b)
            elif form == "Quadrat":
                a = float(eingabefelder['a'].get())
                if a <= 0:
                    raise ValueError
                flaecheninhalt = a ** 2
                ergebnis_feld.config(state="normal")
                ergebnis_feld.delete(0, tk.END)
                ergebnis_feld.insert(0, f"A = {flaecheninhalt:.2f}")
                ergebnis_feld.config(state="readonly")
                zeichne_quadrat(a)
            elif form == "Raute":
                e = float(eingabefelder['e'].get())
                f = float(eingabefelder['f'].get())
                if e <= 0 or f <= 0:
                    raise ValueError
                flaecheninhalt = (e * f) / 2
                ergebnis_feld.config(state="normal")
                ergebnis_feld.delete(0, tk.END)
                ergebnis_feld.insert(0, f"A = {flaecheninhalt:.2f}")
                ergebnis_feld.config(state="readonly")
                zeichne_raute(e, f)
            elif form == "Trapez":
                import numpy as np
                a = float(eingabefelder['a'].get())
                c = float(eingabefelder['c'].get())
                h = float(eingabefelder['h'].get())
                if a <= 0 or c <= 0 or h <= 0 or c < a:
                    raise ValueError
                flaecheninhalt = ((a + c) * h) / 2
                ergebnis_feld.config(state="normal")
                ergebnis_feld.delete(0, tk.END)
                ergebnis_feld.insert(0, f"A = {flaecheninhalt:.2f}")
                ergebnis_feld.config(state="readonly")
                zeichne_trapez_eindeutig(a, c, h)
            elif form == "Deltoid":
                a = float(eingabefelder['a'].get())
                c = float(eingabefelder['c'].get())
                e = float(eingabefelder['e'].get())
                if a <= 0 or c <= 0 or e <= 0:
                    raise ValueError
                # Fläche mit e und berechnetem f
                import numpy as np
                f = 2 * np.sqrt(a**2 - (e/2)**2)
                flaecheninhalt = (e * f) / 2
                ergebnis_feld.config(state="normal")
                ergebnis_feld.delete(0, tk.END)
                ergebnis_feld.insert(0, f"A = {flaecheninhalt:.2f}")
                ergebnis_feld.config(state="readonly")
                zeichne_deltoid_eindeutig(a, c, e)
        except Exception:
            ergebnis_feld.config(state="normal")
            ergebnis_feld.delete(0, tk.END)
            ergebnis_feld.insert(0, "Ungültige Eingabe!")
            ergebnis_feld.config(state="readonly")

    root = tk.Tk()
    root.title("Flächenberechnung")
    root.geometry("520x540")
    root.configure(bg="#f7f7f7")
    auswahl_var = tk.StringVar(value="Dreieck")
    auswahl_label = tk.Label(root, text="Form wählen:", font=("Arial", 15, "bold"), bg="#f7f7f7")
    auswahl_label.pack(pady=(18,2))
    auswahl_box = ttk.Combobox(root, textvariable=auswahl_var, values=["Dreieck", "Rechteck", "Quadrat", "Raute", "Trapez", "Deltoid"], state="readonly", font=("Arial", 13))
    auswahl_box.pack(pady=(0,10))
    haupt_frame = tk.Frame(root, bg="#f7f7f7")
    haupt_frame.pack(fill="both", expand=True, padx=30, pady=10)
    eingabefelder = {}
    ergebnis_label = tk.Label(root, text="A =", font=("Arial", 13, "bold"), bg="#f7f7f7")
    ergebnis_label.pack(pady=(0,0))
    ergebnis_feld = tk.Entry(root, font=("Arial", 13), width=38, bg="#e9e9e9", state="readonly", justify="center")
    ergebnis_feld.pack(pady=(0,10))
    def auswahl_geaendert(event=None):
        zeige_eingabefelder(auswahl_var.get())
    auswahl_box.bind("<<ComboboxSelected>>", auswahl_geaendert)
    zeige_eingabefelder(auswahl_var.get())
    root.mainloop()

if __name__ == "__main__":
    berechne_flaecheninhalt_gui()