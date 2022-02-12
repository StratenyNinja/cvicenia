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