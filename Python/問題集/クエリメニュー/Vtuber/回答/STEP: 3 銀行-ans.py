N, K = map(int, input().split())

data = {}
for _ in range(N):
    c, p, d = input().split()
    data[c] = (p, int(d))

for _ in range(K):
    g, m, w = input().split()

    pin, save = data[g]
    if pin != m:
        continue

    data[g] = (pin, save - int(w))

for name, d in data.items():
    print(name, d[1])