from math import radians, sin, cos


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
    print(f"{i+1}. cifra {cislo[i]}")
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
    print(f"{i:3} {i**2:5} {i**3:7} {i**4:9}")

# 11)
pocet = int(input("zadaj počet: "))
pi = 0
citatel = 4
for i in range(1, 2*pocet, 2):
    pi += citatel/i
    citatel = -citatel
print("pi =", pi)

# 12)
samohlasky = input("zadaj samohlásky: ")
for i in samohlasky:
    print(f"S{i}d{i} m{i}ch{i} n{i} st{i}n{i}, s{i}d{i} {i} sp{i}.")

# 13)
od = int(input("zadaj od: "))
do = int(input("zadaj do: "))
for i in range(od, do+1):
    for j in range(od, do+1):
        print(f"{i*j:4}", end=" ")
    print()
print(f"     | ", end="")
for i in range(od, do+1):
    print(f"{i:4}", end=" ")
print()
print(f"=====|={'='*5*(do-od+1)}")
for i in range(od, do+1):
    print(f"{i:4} | ", end="")
    for j in range(od, do+1):
        print(f"{i*j:4}", end=" ")
    print()

# 14)
od = int(input("zadaj od: "))
do = int(input("zadaj do: "))
krok = int(input("zadaj krok: "))
for i in range(od, do+1, krok):
    rad = radians(i)
    sin2 = sin(rad) ** 2
    cos2 = cos(rad) ** 2
    print(f"{i:3} sin**2={sin2:6.4f} cos**2={cos2:6.4f} súčet={sin2+cos2}")

# 15)


# 16)


# 17)


# 18)


# 19)


# 20)
