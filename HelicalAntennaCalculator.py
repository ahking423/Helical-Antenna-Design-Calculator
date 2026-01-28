# ---Import Libraries---
import math
import tkinter as tk
from tkinter import ttk

# ---Define Function---

def helical(freq, n):
    #Constants
    c = 299792458000 # speed of light in mm/s
    pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280

    # Wavelength
    lam = c / freq # mm

    # Diameter
    D = lam / pi # mm

    # Coil Circumference
    circ = D * pi # mm

    # Coil spacing
    S = lam / 4 # mm

    # Coil Height
    H = S * n # mm

    # Axial Ratio
    Ax = (2 * n + 1) / (2 * n)

    alpha = math.degrees(math.atan(S / circ))

    # Isentropic Gain (dbi)
    G = 10 * math.log(15 * (circ / lam) ** 2 * n * (S / lam), 10) # dbi
    
    return (D, S, H, alpha, Ax, G)

# --- UI Results Inject---
def UIResults(freq, n):
    # Entry Inputs
    freq = float(freq.get())    
    n = float(n.get())
    Unit = UnitSelect.get()

    #Determine Units
    if Unit == 'Hz':
        pass

    elif Unit == 'KHz':
        freq = freq * 10 ** 3

    elif Unit == 'MHz':
        freq = freq * 10 ** 6
    else:
        freq = freq * 10 ** 9

    # Call Helical Function
    D, S, H, Alpha, Axi, Gain = helical(freq, n)

    # Label Inject
    CoilD.config(text=f'{D:.3f} mm')
    CoilS.config(text=f'{S:.3f} mm')
    CoilH.config(text=f'{H:.3f} mm')
    CoilAlpha.config(text=f'{Alpha:.3f} degrees')
    Axial.config(text=f'{Axi:.3f}')
    IGain.config(text=f'{Gain:.3f} ')

# ---GUI with tkinter---
root = tk.Tk()
root.title("Helical Antenna Calculator")
root.geometry("450x400")

# Frequency Input
ttk.Label(root, text='Frequency: ').grid(row=0, column=0, sticky='W', pady=5)
freq = ttk.Entry(root, width=10)
freq.grid(row=0, column=1, pady=5)

units = ['Hz', 'KHz', 'MHz', 'GHz']
UnitSelect = ttk.Combobox(root, values=units, state='readonly')
UnitSelect.grid(row=0, column=2, padx=10, pady=10)
UnitSelect.current(0)

# Number of Coils Input
ttk.Label(root, text='# of Coils: : ').grid(row=2, column=0, sticky='W', pady=5)
n = ttk.Entry(root, width=10)
n.grid(row=2, column=1, pady=5)

# Calculation
CalcButton = ttk.Button(root, text='Calculate', command=lambda: UIResults(freq, n))
CalcButton.grid(row=3, column=0, columnspan=2, pady=10)

# Coil Diameter Output
ttk.Label(root, text='Coil Diameter: ').grid(row=4, column=0, sticky='W', pady=5)
CoilD = ttk.Label(root, width=10)
CoilD.grid(row=4, column=1, pady=5)

# Coil Spacing Output
ttk.Label(root, text='Coil Spacing: ').grid(row=5, column=0, sticky='W', pady=5)
CoilS = ttk.Label(root, width=10)
CoilS.grid(row=5, column=1, pady=5)

# Coil Height Output
ttk.Label(root, text='Coil Height: ').grid(row=6, column=0, sticky='W', pady=5)
CoilH = ttk.Label(root, width=10)
CoilH.grid(row=6, column=1, pady=5)

# Coil Alpha Angle Output
ttk.Label(root, text='Antenna Alpha Value: ').grid(row=7, column=0, sticky='W', pady=5)
CoilAlpha = ttk.Label(root, width=10)
CoilAlpha.grid(row=7, column=1, pady=5)

# Coil Axial Ratio Output
ttk.Label(root, text='Axial Ratio: ').grid(row=8, column=0, sticky='W', pady=5)
Axial = ttk.Label(root, width=10)
Axial.grid(row=8, column=1, pady=5)

# CAntenna Isentropic Gain Output
ttk.Label(root, text='Isentropic Gain: ').grid(row=9, column=0, sticky='W', pady=5)
IGain = ttk.Label(root, width=10)
IGain.grid(row=9, column=1, pady=5)

root.mainloop()