a = [1] * (40 + 1)

for i in range(3, 40 + 1):
    a[i] = a[i - 1] + a[i - 2]

q = int(input())

for i in range(q):
    k = int(input())
    print(a[k])