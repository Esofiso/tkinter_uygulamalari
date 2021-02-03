# GUI: Graphical User Interface
# CLI: Console Line Interface
import tkinter as tk


def fehmiyi_oynat():
    """
    Her 1 saniyede fehmi dayı LABELi sağa kayii, ama sonra yumulii durmii..
    """
    feh.place(x=feh.winfo_x() + 20)
    root.after(500, fehmiyi_oynat)


def fehminin_rengini_degistir():
    """
    Necmi'nin butonu bu. fehmi'nin rengini değiştiriii
    """
    if feh["bg"] == "yellow":
        feh["bg"] = "brown"
        feh["fg"] = "yellow"
    else:
        feh["fg"] = "brown"
        feh["bg"] = "yellow"


# pencereyi oluşturuyoruz
root = tk.Tk()
screen_width, screen_height = 800, 600
root.geometry(f"{screen_width}x{screen_height}")

# FEHMİİ label'i
feh = tk.Label(root, text="FEHMİİ", bg="brown", fg="yellow",
               font=("Times New Roman", 25))
feh.place(x=30, y=120, width=120, height=50)


# Necmi'nin butonu
nec = tk.Button(root, text="Fehmi'nin\nRengini\nAttır", bg="green", fg="blue",
                command=fehminin_rengini_degistir,
                font=("Times New Roman", 35))
nec.place(x=screen_width/2 - 110, y=420, width=220, height=170)

# saniyede 1 oynat
root.after(500, fehmiyi_oynat)

# habire göz kulak ol ne döndüğüne
root.mainloop()
