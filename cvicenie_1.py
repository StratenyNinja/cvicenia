# 1)
a1 = 3 ** (1/2)
a2 = 5 ** (1/3) / 3
a3 = (1024 ** (1/5)) ** 5
a4 = (2 ** 20) ** (1/10)
print('a1 =', a1)
print('a2 =', a2)
print('a3 =', a3)
print('a4 =', a4)

# 2)
pi = 3.141592653589793
pi1 = 223 / 71
pi2 = 22/17 + 37/47 + 88/83
pi3 = 99 ** 2 / (2206 * 2 ** (1/2))
pi4 = ((5 ** (1/2) + 6) ** (1/2) + 7) ** (1/2)
pi5 = (10 ** 100 / 11222.11122) ** (1/193)
print('vzorec č.1 sa od pi líši o', abs(pi - pi1))
print('vzorec č.2 sa od pi líši o', abs(pi - pi2))
print('vzorec č.3 sa od pi líši o', abs(pi - pi3))
print('vzorec č.4 sa od pi líši o', abs(pi - pi4))
print('vzorec č.5 sa od pi líši o', abs(pi - pi5))

# 3)
meno = input('zadaj meno: ')
vek = int(input('zadaj vek: '))
print(meno, 'má', vek, 'rokov')
print(meno, 'bude mať o rok', vek+1)
print(meno, 'bude mať o 10 rokov', vek+10)

# 4)
pi = 3.14159
r = float(input('zadaj polomer: '))
print('obvod je', 2 * pi * r)
print('obsah je', pi * r ** 2)

# 5)
a = float(input('zadaj veľkosť strany kocky: '))
print('stenová uhlopriečka je', round(a * 2 ** (1/2), 2))
print('telesová uhlopriečka je', round(a * 3 ** (1/2), 2))

# 6)
cislo = int(input('zadaj číslo: '))
print(cislo // 10, cislo % 10)
print(cislo // 100, cislo % 100)
print(cislo // 1000, cislo % 1000)
print(cislo // 10000, cislo % 10000)

# 7)
slovo1 = input('zadaj 1. slovo: ')
slovo2 = input('zadaj 2. slovo: ')
slovo3 = input('zadaj 3. slovo: ')
print(slovo1, slovo2, slovo3)
print(slovo1, slovo3, slovo2)
print(slovo2, slovo1, slovo3)
print(slovo2, slovo3, slovo1)
print(slovo3, slovo1, slovo2)
print(slovo3, slovo2, slovo1)

# 8)
txt = input('zadaj text: ') + '\n'
print(txt * 10, end='')

# 9)
dni = 12*365 + 8*30 + 21
hodin = dni * 24
sekund = hodin * 3600
print('počet dní je', dni)
print('počet hodín je', hodin)
print('počet sekúnd je', sekund)

# 10)
b = int(input('zadaj počet bajtov: '))
print('maximálna hodnota je', 256 ** b - 1)

# 11)
n = int(input('zadaj n: '))
print(f'na {n}. políčku bude {2 ** (n-1)} zrniek ryže')
print('na 64. políčku bude', round(2 ** 63 / 50 / 1000000, 2), 'ton ryže')

# 12)
cislo1 = int(input('zadaj 1. číslo: '))
cislo2 = int(input('zadaj 2. číslo: '))
print(f'{cislo1}+{cislo2}={cislo1 + cislo2}')