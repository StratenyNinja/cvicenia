from math import radians, sin, cos
import random


# 1)
n = int(input("zadaj n: "))
for i in range(n):
    print("*" * (i+1))

# 2)
slovo = input("zadaj slovo: ")
for i in range(len(slovo)):
    print(slovo[i] * (i+1))

# 3)
slovo = input("zadaj slovo: ")
for i in range(len(slovo)):
    print(slovo[:i+1])

# 4)
slovo = input("zadaj slovo: ")
n = int(input("zadaj n: "))
for i in range(n):
    print(" " * (i%4*4) + slovo)

# 5)
n = int(input("zadaj n: "))
for i in range(n):
    print(" " * (n-i-1) + "*" * (i*2+1))

# 6)
n = int(input("zadaj n: "))
print(" " * (n-1) + "*")
for i in range(1, n-1):
    print(" " * (n-i-1) + "*" + "-" * (i*2-1) + "*")
print("*" * (n*2-1))

# 7)
cislo = input("zadaj číslo: ")
sucet = 0
for i in range(len(cislo)):
    print(f"{i+1}. cifra", cislo[i])
    sucet += int(cislo[i])
print("ciferný súčet je", sucet)

# 8)
n = int(input("zadaj n: "))
retazec = ""
for i in range(n):
    retazec += "*" * (i+1) + " "
print(retazec)

# 9)
od = int(input("zadaj od: "))
do = int(input("zadaj do: "))
retazec = ""
for i in range(od, do+1):
    retazec += f"<{i}> "
print(retazec)

# 10)
od = int(input("zadaj od: "))
do = int(input("zadaj do: "))
for i in range(od, do+1):
    print(f"{i:3} {i**2:6} {i**3:8} {i**4:10}")

# 11)
pocet = int(input("zadaj počet: "))
pi = 0
citatel = 4
for menovatel in range(1, 2*pocet, 2):
    pi += citatel / menovatel
    citatel = -citatel
print("pi =", pi)

# 12)
samohlasky = input("zadaj samohlásky: ")
for samohlasku in samohlasky:
    print(f"S{i}d{i} m{i}ch{i} n{i} st{i}n{i}, s{i}d{i} {i} sp{i}.")

# 13)
od = int(input("zadaj od: "))
do = int(input("zadaj do: "))
for i in range(od, do+1):
    for j in range(od, do+1):
        print(f"{i*j:4}", end=" ")
    print()
print()

print("     | ", end="")
for i in range(od, do+1):
    print(f"{i:4}", end=" ")
print()
print(f"=====|={'=' * 5 * (do-od+1)}")
for i in range(od, do+1):
    print(f"{i:4} | ", end="")
    for j in range(od, do+1):
        print(f"{i*j:4}", end=" ")
    print()

# 14)
od = int(input("zadaj od: "))
do = int(input("zadaj do: "))
krok = int(input("zadaj krok: "))
for uhol in range(od, do+1, krok):
    rad = radians(uhol)
    sin2 = sin(rad) ** 2
    cos2 = cos(rad) ** 2
    print(f"{uhol:3} sin**2={sin2:6.4f} cos**2={cos2:6.4f} súčet={sin2+cos2}")

# 15)
n = int(input("zadaj n: "))
for i in range(n):
    bod1 = random.randint(0, 100)
    bod2 = random.randint(0, 100)
    print(f"Prvý bod na priamke je {bod1}, druhý bod {bod2}. Ich vzdialenosť je", abs(bod1-bod2))

# 16)
n = int(input("zadaj n: "))
predtym = 100
for i in range(n):
    nastupilo = random.randint(0, 9)
    vystupilo = random.randint(0, 9)
    print(f"Vo vlaku bolo {predtym} ľudí, {nastupilo} nastúpilo, {vystupilo} vystúpilo. Zostalo {predtym+nastupilo-vystupilo}.")
    predtym += nastupilo - vystupilo

# 17)
riadky = int(input("zadaj počet riadkov: "))
stlpce = int(input("zadaj počet stĺpcov: "))
for i in range(riadky):
    for j in range(stlpce):
        print(random.choice("O-"), end="")
    print()

# 18)
n = int(input("zadaj n: "))
for i in range(n):
    kocka1 = random.randint(1, 6)
    kocka2 = random.randint(1, 6)
    print("na 1. kocke padla", kocka1)
    print("na 2. kocke padla", kocka2)
    print("ich súčet je", kocka1 + kocka2)
    print("======================")

# 19)
n = int(input("zadaj n: "))
kocky = int(input("zadaj počet kociek: "))
for i in range(n):
    sucet = 0
    for j in range(kocky):
        cislo = random.randint(1, 6)
        print(f"na {j+1}. kocke padla {cislo}")
        sucet += cislo
    print("ich súčet je", sucet)
    print("======================")

# 20)
n = int(input("zadaj n: "))
for i in range(n):
    for x in range(3):
        for j in range(n):
            print(f"{i*n + j + 1:2}", end=" ")
        print("   ", end="")
    print()