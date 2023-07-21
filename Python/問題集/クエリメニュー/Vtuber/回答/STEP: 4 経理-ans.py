N, K = map(int, input().split())
departments = {input(): [] for _ in range(N)}

for _ in range(K):
	a, p, m = input().split()

	departments[a].append((p,m))

for key, val in departments.items():
	print(key)
	for p, m in val:
		print(p, m)

	print("-----")