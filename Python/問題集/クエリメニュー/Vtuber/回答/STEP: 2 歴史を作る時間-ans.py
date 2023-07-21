N, K = map(int, input().split())
names = [input() for _ in range(N)]

histories = [None] * K
for i in range(K):
    year, charge = input().split()
    histories[i] = (int(year), charge)

for year, name in sorted(histories):
    print(name)