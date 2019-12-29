from random import randint

angka1 = []
angka2 = []

for x in range(1, 50):
    if x % 2 == 0:
        angka1.append(x)
    else:
        angka2.append(x)

print(angka1)

print(angka2)