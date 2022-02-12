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