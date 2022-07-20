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
while n > 1:
    print(n, end=", ")
    if n%2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
print(n)

# 3)
spolu, cislo, x = 0, 1, 1
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
    if cislo%delitel == 0:
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
x, y = 300, 150
while cislo:
    cifra = cislo % 10
    cislo //= 10
    canvas.create_rectangle(x, y, x+30, y+30, fill="lightblue")
    canvas.create_text(x+15, y+15, text=cifra, font="arial 20")
    x -= 35

# 7)
canvas = tk.Canvas()
canvas.pack()
cislo = int(input("zadaj číslo: "))
x, y = 300, 150
while cislo:
    cifra = cislo % 8
    cislo //= 8
    canvas.create_rectangle(x, y, x+30, y+30, fill="lightblue")
    canvas.create_text(x+15, y+15, text=cifra, font="arial 20")
    x -= 35

canvas = tk.Canvas()
canvas.pack()
cislo = int(input("zadaj číslo: "))
x, y = 300, 150
while cislo:
    cifra = cislo % 2
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
            farba = "red"
        else:
            farba = "white"
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)

canvas = tk.Canvas()
canvas.pack()
n = 13
for i in range(n):
    for j in range(n):
        x = j * 20 + 100
        y = i * 20 + 12
        if i == j or j+i == n-1:
            farba = "red"
        else:
            farba = "white"
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
r, k, i = 120, 6, 0
while r > 14:
    if i%k:
        farba = "black"
    else:
        farba = "gray"
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=farba)
    i += 1
    r -= 3

# 11)
canvas = tk.Canvas(width=350, height=260)
canvas.pack()
k = 21
y = 10
for i in range(10):
    x = 10
    sucet = 0
    while sucet < k:
        cislo = random.randint(1, 4)
        canvas.create_oval(x, y, x+20, y+20)
        canvas.create_text(x+10, y+10, text=cislo, font="arial 10")
        sucet += cislo
        x += 25
    if sucet == k:
        txt, farba = "HURÁ", "green"
    else:
        txt, farba = "ŠKODA", "red"
    canvas.create_text(325, y+10, text=txt, font="arial 10", fill=farba)
    y += 25

# 12)
canvas = tk.Canvas(width=300, height=300)
canvas.pack()
for i in range(4000):
    x, y = random.randint(0, 300), random.randint(0, 300)
    if 75 < x < 225 and 75 < y < 225:
        farba = "red"
    else:
        farba = "blue"
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=farba, width=0)

# 13)
canvas = tk.Canvas(width=300, height=300)
canvas.pack()
for i in range(4000):
    x, y = random.randint(0, 300), random.randint(0, 300)
    if x <= y and 300-x < y:
        farba = "green"
    elif x > y and 300-x >= y:
        farba = "blue"
    elif x <= y and 300-x >= y:
        farba = "red"
    else:
        farba = "yellow"
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=farba, width=0)

# 14)
canvas = tk.Canvas(width=300, height=300)
canvas.pack()
x2, y2 = 180, 130
r = 110
for i in range(4000):
    x1, y1 = random.randint(0, 300), random.randint(0, 300)
    if (x1-x2)**2 + (y1-y2)**2 <= r**2:
        farba = "red"
    else:
        farba = "blue"
    canvas.create_oval(x1-5, y1-5, x1+5, y1+5, fill=farba, width=0)

# 15)
canvas = tk.Canvas(width=300, height=300)
canvas.pack()
cervene = 0
for i in range(10000):
    x, y = random.randint(0, 300), random.randint(0, 300)
    if x**2 + y**2 <= 300**2:
        farba = "red"
        cervene += 1
    else:
        farba = "blue"
    canvas.create_oval(x-2, y-2, x+2, y+2, fill=farba, width=0)
print("podiel =", cervene / 10000 * 4)

# 16)
canvas = tk.Canvas(width=300, height=300)
canvas.pack()
n = 7
najm_x, najm_y = 300, 300
najv_x, najv_y = 0, 0
for i in range(n):
    x, y = random.randint(0, 300), random.randint(0, 300)
    if najm_x > x:
        najm_x = x
    if najm_y > y:
        najm_y = y
    if najv_x < x:
        najv_x = x
    if najv_y < y:
        najv_y = y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill="red", width=0)
canvas.create_rectangle(najm_x, najm_y, najv_x, najv_y, outline="blue")

# 17)
canvas = tk.Canvas(width=360, height=260)
canvas.pack()
for i in range(10000):
    x, y = random.randint(10, 350), random.randint(10, 250)
    if y < 90:
        farba = "black"
    elif y < 170:
        farba = "red"
    else:
        farba = "gold"
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=farba, width=0)

# 18)
canvas = tk.Canvas(width=360, height=260)
canvas.pack()
for i in range(10000):
    x, y = random.randint(10, 350), random.randint(10, 250)
    if y < 130:
        if y > x:
            farba = "blue"
        else:
            farba = "white"
    else:
        if 130-x > y-130:
            farba = "blue"
        else:
            farba = "red"
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=farba, width=0)

# 19)
suma = int(input("začínam so sumou: "))
print("štart ", end="")
for i in range(1000):
    suma -= 1
    print("-1", end="")
    c1, c2, c3 = random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)
    if c1 == c2 == c3:
        suma += 100
        print("+100", end="")
    elif c1 == c2 or c1 == c3 or c2 == c3:
        suma += 5
        print("+5", end="")
    if suma == 0:
        break
print("\nzostalo mi", suma, "euro")

# 20)
suma = int(input("zadaj číslo: "))
for bankovka in 100, 50, 20, 10, 5, 2, 1:
    if suma//bankovka != 0:
        print(suma//bankovka, "krát hondota", bankovka)
    suma %= bankovka

# 21)
cislo = float(input("zadaj číslo: "))
x = 0
od, do = 0, cislo
while abs(2**x - cislo) > 0.0001:
    x = (od + do) / 2
    if 2**x > cislo:
        do = x
    else:
        od = x
print("logaritmus", cislo, "je", x)

# 22)
canvas = tk.Canvas(width=300, height=260)
canvas.pack()

a = xa, ya = 10, 100
b = xb, yb = 250, 10
c = xc, yc = 300, 250
while True:
    farba = f'#{random.randrange(256**3):06x}'
    canvas.create_polygon(a, b, c, fill=farba)
    a = (xa+xb)/2, (ya+yb)/2
    b = (xb+xc)/2, (yb+yc)/2
    c = xc, yc = (xc+xa)/2, (yc+ya)/2
    xa, ya = a
    xb, yb = b
    d1 = ((xa-xb)**2 + (ya-yb)**2) ** .5
    d2 = ((xc-xb)**2 + (yc-yb)**2) ** .5
    d3 = ((xa-xc)**2 + (ya-yc)**2) ** .5
    if d1 < 30 or d2 < 30 or d3 < 30:
        break

tk.mainloop()