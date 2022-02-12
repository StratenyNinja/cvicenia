# 1)
a1 = 3 ** (1/2)
a2 = 5 ** (1/3) / 3
a3 = (1024 ** (1/5)) ** 5
a4 = (2 ** 20) ** (1/10)
print(f"a1 = {a1}\na2 = {a2}\na3 = {a3}\na4 = {a4}")

# 2)
pi = 3.141592653589793
pi1 = 223 / 71
pi2 = 22/17 + 37/47 + 88/83
pi3 = 99 ** 2 / (2206 * 2 ** (1/2))
pi4 = ((5 ** (1/2) + 6) ** (1/2) + 7) ** (1/2)
pi5 = (10 ** 100 / 11222.11122) ** (1/193)
print(f"Vzorec č.1 sa od pi líši o {abs(pi - pi1)}")
print(f"Vzorec č.2 sa od pi líši o {abs(pi - pi2)}")
print(f"Vzorec č.3 sa od pi líši o {abs(pi - pi3)}")
print(f"Vzorec č.4 sa od pi líši o {abs(pi - pi4)}")
print(f"Vzorec č.5 sa od pi líši o {abs(pi - pi5)}")

# 3)
meno = input("zadaj meno: ")
vek = int(input("zadaj vek: "))
print(f"{meno.capitalize()} má {vek} rokov.")
print(f"{meno.capitalize()} bude mať o rok {vek + 1}.")
print(f"{meno.capitalize()} bude mať o 10 rokov {vek + 10}.")

# 4)