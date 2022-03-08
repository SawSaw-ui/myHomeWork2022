n = list(range(1, 10001, 2))
print(n)

m = []
for i in n:
    m.append(i ** 3)
print(m)

x = []
total = 0
for digit in m:
    i = digit
    while digit != 0:
        total += digit % 10
        digit = digit // 10
    if total % 7 == 0:
        x.append(i)
    total = 0
print(x)

total2 = 0

for digit in m:
    total = 0
    i = digit
    digit += 17
    while digit != 0:
        total += digit % 10
        digit = digit // 10
    if total % 7 == 0:
        total2 += i + 17

print(total2)