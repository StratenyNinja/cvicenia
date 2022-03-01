import tkinter as tk
import random


# 1)
x = int(input("zadaj km pre prvý deň: "))
y = int(input("zadaj cieľové km: "))
d = 1
while x < y:
    x *= 1.1
    d += 1
print(f"na {d}. deň prebehne {x:.2f} km")

# 2)
n = int(input("zadaj číslo: "))
print(n, end="")
while n > 1:
    if n%2 == 0:
        n //= 2
        print(f", {n}", end="")
    else:
        n = 3*n + 1
        print(f", {n}", end="")

# 3)
cislo, spolu, x = 1, 0, 1
while cislo != 0:
    cislo = float(input(f"zadaj {x}. číslo: "))
    spolu += cislo
    x += 1
print("súčet všetkých prečítaných čísel je", spolu)

# 4)
cislo = int(input("zadaj číslo: "))
print(cislo, end=" ")
delitel = 2
znak = "="
while cislo > 1:
    if cislo % delitel == 0:
        print(znak, delitel, end=" ")
        cislo //= delitel
        znak = "*"
    else:
        delitel += 1

# 5)
cislo = int(input("zadaj číslo: "))
cs = 0
while cislo:
    cifra = cislo % 10
    cs += cifra
    cislo //= 10
    print(cifra)
print("ciferný súčet =", cs)

# 6)
canvas = tk.Canvas()
canvas.pack()
cislo = int(input("zadaj číslo: "))
cs = 0
x, y = 300, 150
while cislo:
    cifra = cislo % 10
    cs += cifra
    cislo //= 10
    canvas.create_rectangle(x, y, x+30, y+30, fill="lightblue")
    canvas.create_text(x+15, y+15, text=cifra, font="arial 20")
    x -= 35

# 7)
canvas = tk.Canvas()
canvas.pack()
cislo = int(input("zadaj číslo: "))
cs = 0
x, y = 300, 150
while cislo:
    cifra = cislo % 8
    cs += cifra
    cislo //= 8
    canvas.create_rectangle(x, y, x+30, y+30, fill="lightblue")
    canvas.create_text(x+15, y+15, text=cifra, font="arial 20")
    x -= 35

canvas = tk.Canvas()
canvas.pack()
cislo = int(input("zadaj číslo: "))
cs = 0
x, y = 300, 150
while cislo:
    cifra = cislo % 2
    cs += cifra
    cislo //= 2
    canvas.create_rectangle(x, y, x+30, y+30, fill="lightblue")
    canvas.create_text(x+15, y+15, text=cifra, font="arial 20")
    x -= 35


tk.mainloop()