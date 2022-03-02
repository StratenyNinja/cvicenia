import tkinter as tk
from random import randint


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

# 8)
canvas = tk.Canvas()
canvas.pack()
n = 13
for i in range(n):
    for j in range(n):
        x = j * 20 + 100
        y = i * 20 + 12
        if i == n//2 or j == n//2:
            farba = 'red'
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)

canvas = tk.Canvas()
canvas.pack()
n = 13
for i in range(n):
    for j in range(n):
        x = j * 20 + 100
        y = i * 20 + 12
        if i == j or j+i == n-1:
            farba = 'red'
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)

# 9)
vyssi, pred, ziak = True, 0, 1
print("zadávaj výšky žiakov")
while True:
    vyska = input(f"    výška {ziak}. žiaka: ")
    if vyska == "":
        break
    vyska = int(vyska)
    if vyska < pred:
        vyssi = False
    pred = vyska
    ziak += 1
if vyssi:
    print("všetci žiaci sú zoradení správne")
else:
    print("žiaci nie sú správne zoradení")

# 10)
canvas = tk.Canvas()
canvas.pack()
x, y = 190, 130
r = 120
k = 6
i = 0
while r > 14:
    if i % k:
        farba = "black"
    else:
        farba = "gray"
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=farba)
    i += 1
    r -= 3

# 11)
canvas = tk.Canvas(width=350, height=275)
canvas.pack()
k = 21
y = 10
for i in range(10):
    x = 10
    sucet = 0
    while sucet < k:
        cislo = randint(1, 4)
        canvas.create_oval(x, y, x+20, y+20)
        canvas.create_text(x+10, y+10, text=cislo, font="arial 10")
        sucet += cislo
        x += 25
    if sucet == k:
        t, f = "HURÁ", "green"
    else:
        t, f = "ŠKODA", "red"
    canvas.create_text(325, y+10, text=t, font="arial 10", fill=f)
    y += 25

# 12)
canvas = tk.Canvas(width=300, height=300)
canvas.pack()
for i in range(4000):
    x = randint(0, 300)
    y = randint(0, 300)
    if 75 < x < 225 and 75 < y < 225:
        f = "red"
    else:
        f = "blue"
    canvas.create_oval(x, y, x+10, y+10, fill=f, width=0)

# 13)
canvas = tk.Canvas(width=300, height=300)
canvas.pack()
for i in range(4000):
    x = randint(0, 300)
    y = randint(0, 300)
    if x <= y and 300 - x < y:
        f = "green"
    elif x > y and 300 - x >= y:
        f = "blue"
    elif x <= y and 300 - x >= y:
        f = "red"
    else:
        f = "yellow"
    canvas.create_oval(x, y, x+10, y+10, fill=f, width=0)

# 14)
canvas = tk.Canvas(width=300, height=300)
canvas.pack()
x0, y0 = 180, 130
r = 110
for i in range(4000):
    x = randint(0, 300)
    y = randint(0, 300)
    if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:
        f = "red"
    else:
        f = "blue"
    canvas.create_oval(x, y, x+10, y+10, fill=f, width=0)

# 15)


tk.mainloop()