N = int(input())
superchats = {}
memberships = []

for i in range(N):
	input_arr = input().split()
	name = input_arr[0]
	verb = input_arr[1]

	if verb == "give":
		money = int(input_arr[2])
		# 過去にスパチャをしていた場合
		if name in superchats:
			superchats[name] = (superchats[name][0]+money, name)

		# 過去にスパチャをしておらず、一見さんの場合
		else:
			superchats[name] = (money, name)

	else:
		memberships.append(name)
# print(superchats["yoyo"])
# print(sorted(superchats, reverse=False))
# print(superchats.items())
for name, money in sorted(superchats.items(), key=lambda x:x[1], reverse = True):
	print(name)

for member in sorted(memberships):
	print(member)