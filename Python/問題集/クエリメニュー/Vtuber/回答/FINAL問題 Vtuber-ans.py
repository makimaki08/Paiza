N = int(input())

superchat = {}
member = set() # 辞書型に変更している

for _ in range(N):
	event = input().split()

	name = event[0]
	verb = event[1]
	if verb == "give":
		money = int(event[2])
		if name not in superchat:
			superchat[name] = (money, name)

		else:
			superchat[name] = (superchat[name][0] + money, name)

	else:
		member.add(name)

for name, money in sorted(superchats.items(), key = lambda x: x[1], reverse = True):
	print(name)

for name in sorted(member):
	print(name)