retazec = input("?")
dlzka = len(retazec)
print("dlzka =", dlzka)
prevrat = retazec[::-1]
print("prevrat =", prevrat)
for riadok in range(dlzka):
    for pismeno in retazec:
        print(f"{pismeno} * ", end="")
    print()
    for pismeno in retazec:
        print(f"* {pismeno} ", end="")
    print()