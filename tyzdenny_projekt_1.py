retazec = input("?")

dlzka_retazca = len(retazec)
print("dlzka =", dlzka_retazca)

iny_retazec = retazec[::-1]
print("prevrat =", iny_retazec)

for riadok in range(dlzka_retazca):
    for pismeno in retazec:
        print(f"{pismeno} * ", end="")
    print()
    for pismeno in retazec:
        print(f"* {pismeno} ", end="")
    print()