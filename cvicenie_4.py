import tkinter
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
print(n, end=", ")
while n != 1:
    if n%2 == 0:
        n //= 2
        print(n, end=", ")
    else:
        n *= 3
        n += 1
        print(n, end=", ")

# 3)
